import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphql import GraphQLError

from api.events.models import Events as EventsModel
from api.room.models import Room as RoomModel
from helpers.calendar.events import RoomSchedules, CalendarEvents
from helpers.email.email import notification
from helpers.calendar.credentials import get_single_calendar_event
from helpers.auth.authentication import Auth
from helpers.calendar.analytics_helper import CommonAnalytics
from helpers.auth.user_details import get_user_from_db
from helpers.pagination.paginate import ListPaginate
from helpers.devices.devices import update_device_last_seen
import pytz
from dateutil import parser
from datetime import datetime, timedelta


class Events(SQLAlchemyObjectType):
    """
        Returns the events payload
    """
    class Meta:
        model = EventsModel


class DailyRoomEvents(graphene.ObjectType):
    """
    Returns days with their events
    """
    day = graphene.String()
    events = graphene.List(Events)


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
        if kwargs.get('check_in_time'):
            update_device_last_seen(info, room_id, kwargs['check_in_time'])
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
        try:
            device_last_seen = parser.parse(
                    kwargs['start_time']) + timedelta(minutes=10)
        except ValueError:
            raise GraphQLError("Invalid start time")
        update_device_last_seen(info, room_id, device_last_seen)
        if not event:
            event = EventsModel(
                event_id=kwargs['event_id'],
                room_id=room_id,
                event_title=kwargs['event_title'],
                start_time=kwargs['start_time'],
                end_time=kwargs['end_time'],
                number_of_participants=kwargs['number_of_participants'],
                checked_in=False,
                cancelled=True,
                auto_cancelled=True)
            event.save()
        calendar_event = get_single_calendar_event(
                                                    kwargs['calendar_id'],
                                                    kwargs['event_id']
                                                )
        event_reject_reason = 'after 10 minutes'
        if not notification.event_cancellation_notification(
                                                            calendar_event,
                                                            room_id,
                                                            event_reject_reason
                                                            ):
            raise GraphQLError("Event cancelled but email not sent")
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
        event.auto_cancelled = True
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


class PaginatedDailyRoomEvents(graphene.ObjectType):
    """
    Paginated result for daily room events
    """
    DailyRoomEvents = graphene.List(DailyRoomEvents)
    has_previous = graphene.Boolean()
    has_next = graphene.Boolean()
    pages = graphene.Int()
    query_total = graphene.Int()


class Query(graphene.ObjectType):
    all_events = graphene.Field(
        PaginatedDailyRoomEvents,
        start_date=graphene.String(),
        end_date=graphene.String(),
        page=graphene.Int(),
        per_page=graphene.Int(),
        description="Query that returns paginated daily room events")

    @Auth.user_roles('Admin', 'Default User')
    def resolve_all_events(self, info, **kwargs):
        page = kwargs.get('page')
        per_page = kwargs.get('per_page')
        if page is not None and page < 1:
            raise GraphQLError("page must be at least 1")
        if per_page is not None and per_page < 1:
            raise GraphQLError("perPage must be at least 1")
        if page and not per_page:
            raise GraphQLError("perPage argument missing")
        if per_page and not page:
            raise GraphQLError("page argument missing")
        user = get_user_from_db()
        start_date, end_date = CommonAnalytics.all_analytics_date_validation(
            self, kwargs['start_date'], kwargs['end_date']
        )
        query = Events.get_query(info)
        all_events, all_dates = CommonAnalytics.get_all_events_and_dates(
            query, start_date, end_date
        )
        events_in_location = CalendarEvents().get_events_in_location(
            user, all_events)
        all_days_events = []
        for date in set(all_dates):
            daily_events = []
            for event in events_in_location:
                CommonAnalytics.format_date(event.start_time)
                event_start_date = parser.parse(
                    event.start_time).astimezone(pytz.utc)
                day_of_event = event_start_date.strftime("%a %b %d %Y")
                if date == day_of_event:
                    daily_events.append(event)
            all_days_events.append(
                DailyRoomEvents(
                    day=date,
                    events=daily_events
                )
            )
            all_days_events.sort(key=lambda x: datetime.strptime(x.day, "%a %b %d %Y"), reverse=True) # noqa
        if page and per_page:
            paginated_events = ListPaginate(
                iterable=all_days_events,
                per_page=per_page,
                page=page)
            has_previous = paginated_events.has_previous
            has_next = paginated_events.has_next
            current_page = paginated_events.current_page
            pages = paginated_events.pages
            query_total = paginated_events.query_total
            return PaginatedDailyRoomEvents(
                                     DailyRoomEvents=current_page,
                                     has_previous=has_previous,
                                     has_next=has_next,
                                     query_total=query_total,
                                     pages=pages)

        return PaginatedDailyRoomEvents(DailyRoomEvents=all_days_events)
