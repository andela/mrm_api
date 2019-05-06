from dateutil.relativedelta import relativedelta
from graphql import GraphQLError
from api.room.models import Room as RoomModel
from api.events.models import Events as EventsModel
from datetime import datetime
from helpers.calendar.credentials import Credentials
from helpers.email.email import event_cancellation_notification


class UpdateRecurringEvent():
    """
    This class is used:
    - to get recurring events from calendar api
    - update them in the events model
    - cancel any room booking for events that have not
    been checked into three consecutive times

    To test the functionality of this class run the command
    'python run_autocancel_room.py' from the root folder
    """

    def get_room_index_from_attendees(self, attendees, calendar_id):
        """
        :param attendees: this a list of attendees of an event
        as returned by the Calendar API
        :param calendar_id: This is the id calendar_id of the
        room whose index you need to get
        :return: The index of the room in the list of attendees
        """
        index_of_room = 0
        for index in range(len(attendees)):
            if attendees[index]["email"] == calendar_id:
                index_of_room = index
                break
        return index_of_room

    def get_all_recurring_events(self, query, start_date, end_date):
        """
        :param query: A room query that allows you to query all
        the active rooms
        :param start_date: the first day from which you want to get
        the recurring events
        :param end_date: the final date upto which you want to get
        the recurring event
        :return: the recurring events within the time frame
        """
        rooms = query.filter_by(state="active")
        credentials = Credentials()
        service = credentials.set_api_credentials()
        recurring_events = []
        for room in rooms:
            events = []
            try:
                events = service.events().list(
                    calendarId=room.calendar_id, timeMax=end_date,
                    timeMin=start_date, singleEvents=True,
                    orderBy='startTime').execute()
            except Exception:
                continue
            for event in events['items']:
                recurring_event_id = event.get("recurringEventId")
                if not event.get("attendees"):
                    continue
                room_index = self.get_room_index_from_attendees(
                    event["attendees"],
                    room.calendar_id
                )
                room_response_status = event.get(
                    "attendees")[room_index]["responseStatus"]
                if recurring_event_id and room_response_status != "declined":
                    recurring_event = {
                        "start_date": event["start"]["dateTime"],
                        "end_date": event["end"]["dateTime"],
                        "room_name": room.name,
                        "event_summary": event.get("summary"),
                        "date_of_event": start_date,
                        "event_id": event.get("id"),
                        "recurring_event_id": recurring_event_id,
                        "room_id": room.id,
                        "calendar_id": room.calendar_id
                    }
                    recurring_events.append(recurring_event)
        return recurring_events

    def update_recurring_event_status(self):
        """
        checks for events to cancel and updates the relevant data
        to the events model
        """
        print("cancelling events...")
        query = RoomModel.query
        now = datetime.utcnow().isoformat()+"Z"
        next_day = (datetime.utcnow() + relativedelta(hours=24)).isoformat()+"Z"
        events = self.get_all_recurring_events(
            query, now, next_day)
        for event in events:
            start_date = event["start_date"]
            end_date = event["end_date"]
            new_recurring_event = EventsModel(
                event_id=event["event_id"],
                recurring_event=event["recurring_event_id"],
                room_id=event["room_id"],
                event_title=event["event_summary"],
                start_time=start_date,
                end_time=end_date,
                checked_in=False,
                cancelled=False)
            event_query = EventsModel.query
            calendar_id = event["calendar_id"]
            recurring_event_id = event["recurring_event_id"]
            service = Credentials().set_api_credentials()
            missed_checkins = event_query.filter(
                EventsModel.recuring_event_id == event["recurring_event_id"] and
                EventsModel.checked_in == "False")
            if missed_checkins.count() >= 3:
                event = service.events().get(
                    calendarId=calendar_id,
                    eventId=recurring_event_id
                ).execute()
                attendees = event["attendees"]
                room_index = self.get_room_index_from_attendees(
                    attendees,
                    calendar_id
                )
                event["attendees"][room_index]["responseStatus"] = "declined"
                service.events().patch(
                    calendarId=calendar_id,
                    eventId=recurring_event_id,
                    body=event,
                    sendUpdates="all").execute()
                event_in_database = EventsModel.query.filter_by(
                    id=event.get("id")
                ).first()
                room_id = event_in_database.room_id
                event_reject_reason = "for 3 consecutive meetings"
                if not event_cancellation_notification(
                    event, room_id, event_reject_reason
                ):
                    raise GraphQLError("Event cancelled but email not sent")
                for missed_checkin in missed_checkins:
                    missed_checkin.state = "archived"
                    missed_checkin.save()
            else:
                event_exists = event_query.filter_by(
                    event_id=event["event_id"]
                )
                if not event_exists.count():
                    new_recurring_event.save()
