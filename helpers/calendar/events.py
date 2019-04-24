import datetime
import re

import pytz
from dateutil import parser
from graphql import GraphQLError

from api.events.models import Events as EventsModel
from api.room.models import Room as RoomModel
from .analytics_helper import CommonAnalytics
from .credentials import Credentials, get_google_calendar_events


class RoomSchedules(Credentials):
    """Create and get room schedules
       :methods
           create_room_event_schedules
           get_room_event_schedules
    """

    # define schedule methods here
    def get_room_schedules(self, calendar_id, days):
        """ Get room occupants. This method is responsible
            for getting all  occupants of a room in an event.
         :params
            - calendar_id
            - days(Time limit for the schedule you need)
        """
        # 'Z' indicates UTC time
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        new_time = (datetime.datetime.now() + datetime.timedelta(days=days)
                    ).isoformat() + 'Z'
        events_result = get_google_calendar_events(calendarId=calendar_id,
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
                events_result = CommonAnalytics.get_all_events_in_a_room(
                    self, room.id, start_date, end_date)
            except GraphQLError:
                continue
            for event in events_result:
                CommonAnalytics.format_date(event["event_start_time"])
                event_start_date = parser.parse(
                    event["event_start_time"]).astimezone(pytz.utc)
                event_end_date = parser.parse(
                    event["event_end_time"]
                ).astimezone(pytz.utc)
                day_of_event = event_start_date.strftime("%a %b %d %Y")
                all_dates.append(day_of_event)
                current_event = {
                    "start_time": event_start_date.time(),
                    "end_time": event_end_date.time(),
                    "no_of_participants": event['participants'],
                    "room_name": room.name,
                    "event_summary": event['event_title'],
                    "date_of_event": day_of_event,
                    "event_id": event['event_id'],
                    "state": event['state'],
                    "checked_in": event['checked_in_status'],
                    "cancelled": event['cancelled_status'],
                    "check_in_time": event['check_in_time'],
                    "meeting_end_time": event['meeting_end_time'],
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


class CalendarEvents:
    """
    Sync all calendar events with Converge Database
    :methods
        sync_single_room_events
        sync_all_events
    """

    def sync_single_room_events(self, room):
        """
        This method gets data from the calendar api
        and syncs it with the local data

        """
        next_page = None
        next_sync_token = None
        while True:
            event_results = get_google_calendar_events(
                calendarId=room.calendar_id,
                syncToken=room.next_sync_token,
                pageToken=next_page)

            next_page = event_results.get("nextPageToken")
            room_events = event_results["items"]
            next_sync_token = event_results.get("nextSyncToken")
            for event in room_events:
                existing_event = EventsModel.query.filter_by(
                    event_id=event.get("id")
                ).first()
                participants = event.get('attendees')
                number_of_attendees = 0
                if participants:
                    number_of_attendees = len(participants)

                if existing_event and event.get("status") == "cancelled":
                    existing_event.state = "archived"
                    existing_event.save()

                elif existing_event:
                    existing_event.event_title = event.get("summary")
                    existing_event.start_time = event["start"].get(
                        "dateTime") or event["start"].get("date")
                    existing_event.end_time = event["end"].get(
                        "dateTime") or event["end"].get("date")
                    existing_event.number_of_participants = number_of_attendees
                    existing_event.save()

                elif not event.get("status") == "cancelled":
                    new_event = EventsModel(
                        event_id=event.get("id"),
                        recurring_event_id=event.get("recurringEventId"),
                        room_id=room.id,
                        event_title=event.get("summary"),
                        start_time=event["start"].get(
                            "dateTime") or event["start"].get("date"),
                        end_time=event["end"].get(
                            "dateTime") or event["end"].get("date"),
                        number_of_participants=number_of_attendees,
                        checked_in=False,
                        cancelled=False
                    )
                    new_event.save()
            if not next_page:
                break

        room.next_sync_token = next_sync_token
        room.save()

    def sync_all_events(self):
        """
        This method sync the calendar events for all rooms
        within the database
        :return:
        """
        rooms = RoomModel.query.filter_by(state='active')
        for room in rooms:
            self.sync_single_room_events(room)
