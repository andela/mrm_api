from datetime import datetime
import dateutil.parser

from .credentials import Credentials
from api.location.models import Location as LocationModel
from ..room_filter.room_filter import room_join_location


class RoomAnalytics(Credentials):
    """Get room analytics
       :methods
           get_least_used_room_week
    """

    def get_time_duration_for_event(self, start_time, end_time):
        """ Calculate duration range of an event
         :params
            - start_time
            - end_time
        """
        start_time = dateutil.parser.parse(start_time)
        end_time = dateutil.parser.parse(end_time)
        event_duration = end_time - start_time
        return event_duration.seconds / 60

    def get_calendar_id_name(self, query, location_id):
        """ Get all room(name, calendar_id) in a location
         :params
            - location_id
        """
        exact_query = room_join_location(query)
        rooms_in_locations = exact_query.filter(LocationModel.id == location_id)
        result = []
        for room in rooms_in_locations.all():
            room_details = {}
            room_details['name'] = room.name
            room_details['calendar_id'] = room.calendar_id
            result.append(room_details)
        return result

    def get_all_events_in_a_room(self, calendar_id, min_limit, max_limit):
        """ Get all events in a room
         :params
            - calendar_id - for specific room
            - min_limit, max_limit(Time range)
        """
        service = Credentials.set_api_credentials(self)
        events_result = service.events().list(
            calendarId=calendar_id, timeMin=min_limit, timeMax=max_limit,
            singleEvents=True, orderBy='startTime').execute()
        calendar_events = events_result.get('items', [])
        return calendar_events

    def get_event_details(self, event):
        """ Filter details of an event
         :params
            - event
        """
        event_details = {}
        if event.get('attendees'):
            for resource in event.get('attendees'):
                if resource.get('resource'):
                    event_details["minutes"] = RoomAnalytics.get_time_duration_for_event(  # noqa: E501
                        self, event['start'].get(
                            'dateTime'), event['end'].get('dateTime')
                    )
                    event_details["roomName"] = resource.get(
                        'displayName') or None
            event_details["summary"] = event.get("summary")
        return event_details

    def get_room_statistics(self, number_of_events, all_details):
        """ Get summary statistics for room
         :params
            - number_of_events
            - all_details(List of list of events in a room)
        """
        result = []
        for room_details in all_details:
            if len(room_details) == number_of_events:
                output = {
                    'RoomName': room_details[0]['roomName'],
                    'count': number_of_events
                }
                events = {}
                for detail in room_details:
                    if str(detail['minutes']) not in events.keys():
                        events[str(detail['minutes'])] = 1
                    else:
                        events[str(detail['minutes'])] = events[str(
                            detail['minutes'])] + 1
                output['Events in minutes'] = events
                result.append(output)
        return result

    def get_least_used_room_week(self, query, location_id, week_start, week_end):  # noqa: E501
        """ Get analytics for least used room per week
         :params
            - calendar_id, location_id
            - week_start, week_end(Time range)
        """
        week_start = datetime.strptime(
            week_start, '%b %d %Y').isoformat() + 'Z'
        week_end = datetime.strptime(
            week_end, '%b %d %Y').isoformat() + 'Z'

        rooms_available = RoomAnalytics.get_calendar_id_name(
            self, query, location_id)
        res = []
        no_least_events = float("inf")
        for room in rooms_available:
            calendar_events = RoomAnalytics.get_all_events_in_a_room(
                self, room['calendar_id'], week_start, week_end)
            output = []
            if not calendar_events:
                output.append({})
            for event in calendar_events:
                event_details = RoomAnalytics.get_event_details(self, event)
                output.append(event_details)
            if len(output) < no_least_events:
                no_least_events = len(output)
            res.append(output)
        analytics = RoomAnalytics.get_room_statistics(
            self, no_least_events, res)
        return analytics
