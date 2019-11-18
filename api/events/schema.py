import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphql import GraphQLError
import pytz
from dateutil import parser
from datetime import timedelta
from graphene import String

from api.events.models import Events as EventsModel
from api.room.models import Room as RoomModel
from api.events.models import (
    filter_event
)
from helpers.calendar.events import RoomSchedules, CalendarEvents
from helpers.email.email import notification
from helpers.calendar.credentials import (
    get_single_calendar_event,
    credentials
)
from helpers.auth.authentication import Auth
from helpers.pagination.paginate import ListPaginate
from helpers.devices.devices import update_device_last_activity
from helpers.events_filter.events_filter import (
    sort_events_by_date,
    validate_page_and_per_page,
    validate_calendar_id_input
)
from helpers.events_filter.events_filter import (
    calendar_dates_format,
    empty_string_checker
)

utc = pytz.utc


class Events(SQLAlchemyObjectType):
    """
        Returns the events payload
    """
    class Meta:
        model = EventsModel


class BookEvent(graphene.Mutation):
    """
        Book Calendar events
    """
    response = graphene.String()

    class Arguments:
        event_title = graphene.String(required=True)
        start_date = graphene.String(required=True)
        start_time = graphene.String(required=True)
        duration = graphene.Float(required=False)
        attendees = graphene.String(required=False)
        organizer = graphene.String(required=False)
        description = graphene.String(required=False)
        room = graphene.String(required=True)
        time_zone = graphene.String(required=True)

    @Auth.user_roles('Admin', 'Default User', 'Super Admin')
    def mutate(self, info, **kwargs):
        """Creates calendar events

        Args:
            event_title: A sting that communicates the event summary/title
            [required]
            start_date: The start date of the event eg. 'Nov 4 2019' [required]
            start_time: The end time of the event eg '07:00 AM' [required]
            duration: A float of the duration of the event in minutes
            attendees: A string of emails of the event guests
            description: Any additional information about the event
            room: The meeting room where the even will be held [required]
            time_zone: The timezone of the event location eg. 'Africa/Kigali'
            organizer: The email of the co-organizer, the converge email is
            the default

        Returns:
            A string that communicates a successfully created event.
        """
        room = kwargs.get('room', None)
        attendees = kwargs.get('attendees', None)
        description = kwargs.get('description', None)
        time_zone = kwargs.get('time_zone', 'Africa/Accra')
        duration = kwargs.get('duration', 60)
        organizer = kwargs.get('organizer', None)

        event_title = kwargs['event_title']
        empty_string_checker(event_title)
        empty_string_checker(room)
        empty_string_checker(time_zone)

        start_date, end_date = calendar_dates_format(
            kwargs['start_date'], kwargs['start_time'], duration)

        attendees = attendees.replace(" ", "").split(",")
        guests = []
        for guest in attendees:
            attendee = {'email': guest}
            guests.append(attendee)

        event = {
            'summary': kwargs['event_title'],
            'location': room,
            'description': description,
            'start': {
                'dateTime': start_date,
                'timeZone': time_zone,
            },
            'end': {
                'dateTime': end_date,
                'timeZone': time_zone,
            },
            'attendees': guests,
            "organizer": {
                "email": organizer
            }
        }
        service = credentials.set_api_credentials()
        service.events().insert(calendarId='primary', body=event,
                                sendNotifications=True).execute()
        return BookEvent(response='Event created successfully')


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
            update_device_last_activity(
                info, room_id, kwargs['check_in_time'], 'check in')
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
        update_device_last_activity(
            info, room_id, device_last_seen, 'cancel meeting')
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
        if kwargs.get('meeting_end_time'):
            update_device_last_activity(
                info, room_id, kwargs['meeting_end_time'], 'end meeting')
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
        room = RoomModel.query.filter_by(
            calendar_id=calendar_id, state="active").first()
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
    book_event = BookEvent.Field(
        description="Mutation to book a calendar event given the arguments\
            \n- event_title: A sting that communicates the event\
            summary/title [required]\n- start_date: The start date \
                 of the event eg 'Nov 4 2019' [required]\
            \n- start_time: The end time of the event eg'07:00 AM'[required]\
            \n- duration: A float of the duration of the event in minutes\
            \n- attendees: A string of emails of the event guests\
            \n- description: Any additional information about the event\
            \n- room: The meeting room where the even will be held[required]\
            \n- organizer: The email of the co - organizer, the converge\
                email is the default\
            \n- time_zone: The timezone of the event location")
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


class PaginateEvents(graphene.ObjectType):
    """
        Paginate the number of events returned
    """
    events = graphene.List(Events)
    pages = graphene.Int()
    query_total = graphene.Int()
    has_next = graphene.Boolean()
    has_previous = graphene.Boolean()


class RoomEvents(graphene.ObjectType):
    """
        Return all events in a room
    """
    events = graphene.List(Events)


class Query(graphene.ObjectType):
    all_events = graphene.Field(
        PaginateEvents,
        page=graphene.Int(),
        per_page=graphene.Int(),
        start_date=graphene.String(),
        end_date=graphene.String(),
        description="Query that returns a list of events given the arguments\
            \n- start_date: The date and time to start selection in range \
                            when filtering by the time period\
            \n- end_date: The date and time to end selection in range \
                            when filtering by the time period\
            \n- page: Page number to select when paginating\
            \n- per_page: The maximum number of events per page when paginating")  # noqa

    all_events_by_room = graphene.Field(
        RoomEvents,
        calendar_id=String(),
        start_date=String(),
        end_date=String(),
        description="Query that returns a list of events given the arguments\
            \n- calendar_id: The room calendar Id\
            \n- start_date: The date and time to start selection in range \
                            when filtering by the time period\
            \n- end_date: The date and time to end selection in range \
                            when filtering by the time period")

    @Auth.user_roles('Admin', 'Default User', 'Super Admin')
    def resolve_all_events(self, info, **kwargs):
        start_date = kwargs.get('start_date')
        end_date = kwargs.get('end_date')
        page = kwargs.get('page')
        per_page = kwargs.get('per_page')
        page, per_page = validate_page_and_per_page(page, per_page)
        response = filter_event(
           start_date, end_date
        )
        sort_events_by_date(response)

        if page and per_page:
            paginated_response = ListPaginate(
                iterable=response,
                per_page=per_page,
                page=page)
            current_page = paginated_response.current_page
            has_previous = paginated_response.has_previous
            has_next = paginated_response.has_next
            pages = paginated_response.pages
            query_total = paginated_response.query_total
            return PaginateEvents(
                events=current_page,
                has_previous=has_previous,
                has_next=has_next,
                query_total=query_total,
                pages=pages)

        return PaginateEvents(events=response)

    @Auth.user_roles('Admin', 'Super Admin')
    def resolve_all_events_by_room(self, info, **kwargs):
        calendar_id = kwargs.get('calendar_id')
        validate_calendar_id_input(calendar_id)
        start_date = kwargs.get('start_date')
        end_date = kwargs.get('end_date')
        room = RoomModel.query.filter_by(
            calendar_id=calendar_id
        ).first()
        if not room:
            raise GraphQLError("No rooms with the given CalendarId")
        response = filter_event(
            start_date, end_date, room.id
        )
        sort_events_by_date(response)

        return RoomEvents(events=response)
