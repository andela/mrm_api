import datetime
import re
import pytz
from dateutil import parser
from graphql import GraphQLError

from .analytics_helper import CommonAnalytics
from .credentials import Credentials


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
        service = Credentials.set_api_credentials(self)
        # 'Z' indicates UTC time
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        new_time = (datetime.datetime.now() + datetime.timedelta(days=days)
                    ).isoformat() + 'Z'
        events_result = service.events().list(
            calendarId=calendar_id, timeMin=now, timeMax=new_time,
            singleEvents=True, orderBy='startTime').execute()
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
                    "date_of_event": day_of_event
                }
                all_events.append(current_event)

        return all_events, all_dates

    def get_all_recurring_events(self, query, start_date, end_date):
        """ get all recurring events"""
        rooms = query.filter_by(state="active")
        credentials = Credentials()
        service = credentials.set_api_credentials()
        recurring_events = []
        for room in rooms:
            events = service.events().list(
                calendarId=room.calendar_id, timeMax=end_date,
                timeMin=start_date, singleEvents=True,
                orderBy='startTime').execute()
            for event in events['items']:
                check_recurring_event = event.get("recurringEventId")
                if type(check_recurring_event) is str:
                    recurring_event = {
                        "start_date": event["start"]["dateTime"],
                        "end_date": event["end"]["dateTime"],
                        "room_name": room.name,
                        "event_summary": event.get("summary"),
                        "date_of_event": start_date,
                        "event_id": event.get("id"),
                        "recurring_event_id": check_recurring_event
                        }
                    recurring_events.append(recurring_event)
                else:
                    raise GraphQLError("There are no recurring events")
        return recurring_events
