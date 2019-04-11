import datetime
import re
import pytz
from dateutil import parser
from graphql import GraphQLError

from api.room.models import Room as RoomModel
from api.events.models import Events as EventsModel
from .analytics_helper import CommonAnalytics
from .credentials import Credentials, get_events_within_datetime_range


class RoomSchedules(Credentials):
    """Create and get room schedules
       :methods
           create_room_event_schedules
           get_room_event_schedules
    """

    # define schedule methods here
    def get_room_schedules(self, calendar_id, days):
        """ Get room schedules. This method is responsible
            for getting all  occupants of a room in an event.
         :params
            - calendar_id
            - days(Time limit for the schedule you need)
        """
        # 'Z' indicates UTC time
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        new_time = (datetime.datetime.now() + datetime.timedelta(days=days)
                    ).isoformat() + 'Z'
        events_result = get_events_within_datetime_range(calendarId=calendar_id,
                                                         timeMin=now,
                                                         timeMax=new_time,
                                                         singleEvents=True,
                                                         orderBy='startTime')
        calendar_events = events_result.get('items', [])
        output = []
        if not calendar_events:
            return ('No upcoming events found.')
        for event in calendar_events:
            event_details = {}
            event_details["start"] = event['start'].get('dateTime', event['start'].get('date'))  # noqa: E501
            event_details["summary"] = event.get("summary")
            output.append(event_details)

        # Define Attendees here
        for event in calendar_events:
            all_attendees = []
            if event.get('attendees'):
                for attendee in event['attendees']:
                    attendees = attendee.get('email', attendee.get('email'))
                    match = re.match(
                        r"(^[a-zA-Z0-9_.+-]+@andela+\.com+$)", attendees)
                    if match:
                        all_attendees.append(attendee.get('email'))
        return [all_attendees, output]

    def get_all_room_schedules(self, query, start_date, end_date):
        rooms = query.filter_by(state="active")
        all_events = []
        all_dates = []
        for room in rooms:
            try:
                events_result = CommonAnalytics().get_all_events_in_a_room(
                    calendar_id=room.calendar_id,
                    min_limit=start_date,
                    max_limit=end_date
                )
            except GraphQLError:
                continue
            for event in events_result:
                CommonAnalytics.format_date(event["start"]["dateTime"])
                event_start_date = parser.parse(
                    event["start"]["dateTime"]).astimezone(pytz.utc)
                event_end_date = parser.parse(
                    event["end"]["dateTime"]
                ).astimezone(pytz.utc)
                day_of_event = event_start_date.strftime("%a %b %d %Y")
                all_dates.append(day_of_event)
                attendees = event.get("attendees")
                no_of_attendees = 0
                if attendees:
                    no_of_attendees = len(attendees)
                current_event = {
                    "start_time": event_start_date.time(),
                    "end_time": event_end_date.time(),
                    "no_of_participants": no_of_attendees,
                    "room_name": room.name,
                    "event_summary": event.get("summary"),
                    "date_of_event": day_of_event,
                    "event_id": event.get("id"),
                }
                all_events.append(current_event)

        return all_events, all_dates

    def check_event_status(self, info, **kwargs):
        try:
            room_id = RoomModel.query.filter_by(
                calendar_id=kwargs['calendar_id']).first().id
            checked_in_events = EventsModel.query.filter_by(
                    event_id=kwargs['event_id'],
                    room_id=room_id,
                    start_time=kwargs['start_time'],
                    checked_in=True).count()
            cancelled_events = EventsModel.query.filter_by(
                event_id=kwargs['event_id'],
                room_id=room_id,
                start_time=kwargs['start_time'],
                cancelled=True).count()
            if checked_in_events > 0 and 'meeting_end_time' not in kwargs:
                raise GraphQLError("Event already checked in")
            elif checked_in_events < 1 and 'meeting_end_time' in kwargs:
                raise GraphQLError("Event yet to be checked in")
            elif cancelled_events > 0:
                raise GraphQLError("Event already cancelled")
            return room_id
        except AttributeError:
            raise GraphQLError(
                "This Calendar ID is invalid")
