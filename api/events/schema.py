import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphql import GraphQLError

from api.events.models import Events as EventsModel
from api.room.models import Room as RoomModel
from helpers.calendar.events import RoomSchedules, CalendarEvents


class Events(SQLAlchemyObjectType):
    """
        Returns the events payload
    """
    class Meta:
        model = EventsModel


class EventCheckin(graphene.Mutation):
    """
        Returns the eventcheckin payload
    """
    class Arguments:
        calendar_id = graphene.String(required=True)
        event_id = graphene.String(required=True)
        event_title = graphene.String(required=True)
        start_time = graphene.String(required=True)
        end_time = graphene.String(required=True)
        number_of_participants = graphene.Int(required=True)
        check_in_time = graphene.String(required=False)
    event = graphene.Field(Events)

    def mutate(self, info, **kwargs):
        room_id, event = check_event_in_db(self, info, "checked_in", **kwargs)
        if not event:
            event = EventsModel(
                event_id=kwargs['event_id'],
                room_id=room_id,
                event_title=kwargs['event_title'],
                start_time=kwargs['start_time'],
                end_time=kwargs['end_time'],
                number_of_participants=kwargs['number_of_participants'],
                checked_in=True,
                cancelled=False)
            event.save()
        return EventCheckin(event=event)


class CancelEvent(graphene.Mutation):
    """
        Returns the payload on event cancelation
    """
    class Arguments:
        calendar_id = graphene.String(required=True)
        event_id = graphene.String(required=True)
        event_title = graphene.String(required=True)
        start_time = graphene.String(required=True)
        end_time = graphene.String(required=True)
        number_of_participants = graphene.Int()
    event = graphene.Field(Events)

    def mutate(self, info, **kwargs):
        # mutation to create an event
        room_id, event = check_event_in_db(self, info, "cancelled", **kwargs)
        if not event:
            event = EventsModel(
                event_id=kwargs['event_id'],
                room_id=room_id,
                event_title=kwargs['event_title'],
                start_time=kwargs['start_time'],
                end_time=kwargs['end_time'],
                number_of_participants=kwargs['number_of_participants'],
                checked_in=False,
                cancelled=True)
            event.save()

        return CancelEvent(event=event)


class EndEvent(graphene.Mutation):
    """
    Mutation to end an event
    Returns event payload on ending the event
    """
    class Arguments:
        calendar_id = graphene.String(required=True)
        event_id = graphene.String(required=True)
        start_time = graphene.String(required=True)
        end_time = graphene.String(required=True)
        meeting_end_time = graphene.String(required=True)
    event = graphene.Field(Events)

    def mutate(self, info, **kwargs):
        room_id, event = check_event_in_db(self, info, "ended", **kwargs)
        if not event:
            event = EventsModel(
                event_id=kwargs['event_id'],
                meeting_end_time=kwargs['meeting_end_time']
                )
            event.save()

        return EndEvent(event=event)


class SyncEventData(graphene.Mutation):
    """
    Mutation to sync the event data in the db
    with the one on google calendar
    """
    message = graphene.String()

    def mutate(self, info):
        CalendarEvents().sync_all_events()
        return SyncEventData(message="success")


class MrmNotification(graphene.Mutation):
    """
    Mutation to receive notification from MRM_PUSH
    service
    """
    message = graphene.String()

    class Arguments:
        calendar_id = graphene.String()

    def mutate(self, info, calendar_id):
        room = RoomModel.query.filter_by(calendar_id=calendar_id).first()
        CalendarEvents().sync_single_room_events(room)
        return MrmNotification(message="success")


def check_event_in_db(instance, info, event_check, **kwargs):
    room_id = RoomSchedules().check_event_status(info, **kwargs)
    event = EventsModel.query.filter_by(
        start_time=kwargs['start_time'],
        event_id=kwargs['event_id']).scalar()
    if event and event_check == 'cancelled':
        event.cancelled = True
        event.save()
        return room_id, event
    elif event and event_check == 'checked_in':
        event.checked_in = True
        if 'check_in_time' in kwargs:
            event.check_in_time = kwargs['check_in_time']
        else:
            event.check_in_time = None
        event.save()
        return room_id, event
    elif event and event_check == 'ended':
        if event.meeting_end_time:
            raise GraphQLError("Event has already ended")
        event.meeting_end_time = kwargs['meeting_end_time']
        event.save()
        return room_id, event
    return room_id, event


class Mutation(graphene.ObjectType):
    event_checkin = EventCheckin.Field()
    cancel_event = CancelEvent.Field()
    end_event = EndEvent.Field(
        description="Mutation to end a calendar event given the arguments\
            \n- calendar_id: The unique identifier of the calendar event\
            [required]\n- event_id: The unique identifier of the target\
                 calendar event[required]\
            \n- event_id: The unique identifier of the calendar event[required]\
            \n- start_time: The start time of the calendar event[required]\
            \n- end_time: The field with the end time of the calendar event\
            [required]\
            \n- meeting_end_time: The time the calendar event ended[required]")
    sync_event_data = SyncEventData.Field()
    mrm_notification = MrmNotification.Field()
    event_checkin = EventCheckin.Field(
        description="Mutation to check in to a calendar event given the arguments\
            \n- calendar_id: The unique identifier of the calendar event\
            [required]\n- event_id: The unique identifier of the target\
                 calendar event[required]\
            \n- event_title: The title field of the calendar event[required]\
            \n- start_time: The start time of the calendar event[required]\
            \n- end_time: The field with the end time of the calendar event\
            [required]")
    cancel_event = CancelEvent.Field(
        description="Mutation to cancel a claendar event given the arguments\
            \n- calendar_id: The unique identifier of the calendar event\
            [required]\n- event_id: The unique identifier of the target \
                calendar event\
            [required]\n- event_title: The title field of the calendar event\
            [required]\n- start_time: The start time of the calendar event\
            [required]\n- end_time: The field with the end time of the calendar\
             event[required]")
