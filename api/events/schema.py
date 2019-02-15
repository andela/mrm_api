import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType

from api.events.models import Events as EventsModel
from helpers.calendar.events import RoomSchedules


class Events(SQLAlchemyObjectType):
    class Meta:
        model = EventsModel


class EventCheckin(graphene.Mutation):
    class Arguments:
        calendar_id = graphene.String(required=True)
        event_id = graphene.String(required=True)
        event_title = graphene.String(required=True)
        start_time = graphene.String(required=True)
        end_time = graphene.String(required=True)
    event = graphene.Field(Events)

    def mutate(self, info, **kwargs):
        room_id = RoomSchedules().check_event_status(info, **kwargs)
        event = EventsModel.query.filter_by(
            start_time=kwargs['start_time'],
            event_id=kwargs['event_id']).scalar()
        if event is not None:
            event.checked_in = True
            event.save()
        else:
            event = EventsModel(
                event_id=kwargs['event_id'],
                room_id=room_id,
                event_title=kwargs['event_title'],
                start_time=kwargs['start_time'],
                end_time=kwargs['end_time'],
                checked_in=True,
                cancelled=False)
            event.save()
        return EventCheckin(event=event)


class CancelEvent(graphene.Mutation):
    class Arguments:
        calendar_id = graphene.String(required=True)
        event_id = graphene.String(required=True)
        event_title = graphene.String(required=True)
        start_time = graphene.String(required=True)
        end_time = graphene.String(required=True)
    event = graphene.Field(Events)

    def mutate(self, info, **kwargs):
        room_id = RoomSchedules().check_event_status(info, **kwargs)
        cancelled_event = EventsModel(
            event_id=kwargs['event_id'],
            room_id=room_id,
            event_title=kwargs['event_title'],
            start_time=kwargs['start_time'],
            end_time=kwargs['end_time'],
            checked_in=False,
            cancelled=True)
        cancelled_event.save()

        return CancelEvent(event=cancelled_event)


class Mutation(graphene.ObjectType):
    event_checkin = EventCheckin.Field()
    cancelled_event = CancelEvent.Field()
