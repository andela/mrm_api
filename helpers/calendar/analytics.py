from datetime import datetime
import dateutil.parser
from dateutil.relativedelta import relativedelta
from graphql import GraphQLError
import graphene
from collections import Counter

from .credentials import Credentials
from api.location.models import Location as LocationModel
from ..room_filter.room_filter import room_join_location


class EventsDuration(graphene.ObjectType):
    duration_in_minutes = graphene.Int()
    number_of_meetings = graphene.Int()


class RoomStatistics(graphene.ObjectType):
    room_name = graphene.String()
    count = graphene.Int()
    events = graphene.List(EventsDuration)
    has_events = graphene.Boolean()


class RoomAnalytics(Credentials):
    """Get room analytics
       :methods
           get_least_used_room_week
    """

    def convert_date(self, date):
        return datetime.strptime(date, '%b %d %Y').isoformat() + 'Z'

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
        if not rooms_in_locations.all():
            raise GraphQLError("No rooms in this location")
        result = [{'name': room.name, 'calendar_id': room.calendar_id}
                  for room in rooms_in_locations.all()]
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

    def get_event_details(self, event, calendar_id):
        """ Filter details of an event
         :params
            - event
        """
        event_details = {}
        if event.get('attendees'):
            for resource in event.get('attendees'):
                if resource.get('resource') and resource.get('email') == calendar_id:  # noqa: E501
                    event_details["minutes"] = RoomAnalytics.get_time_duration_for_event(  # noqa: E501
                        self, event['start'].get(
                            'dateTime'), event['end'].get('dateTime')
                    )
                    event_details["roomName"] = resource.get(
                        'displayName') or None
                    event_details["summary"] = event.get("summary")
        return event_details

    def get_room_statistics(self, number_of_events_in_room, all_details):
        """ Get summary statistics for room
         :params
            - number_of_events_in_room
            - all_details(List of list of events in a room)
        """
        result = []
        for room_details in all_details:
            if number_of_events_in_room == 0:
                for detail in room_details:
                    if 'has_events' in detail.keys():
                        output = RoomStatistics(
                            room_name=detail['RoomName'],
                            has_events=detail['has_events'],
                            count=0)
                        result.append(output)
            elif len(room_details) == number_of_events_in_room and 'has_events' not in room_details[0].keys():  # noqa: E501
                events_count = Counter(detail['minutes']
                                       for detail in room_details if detail)
                duration_of_events_in_room = [
                    EventsDuration(
                        duration_in_minutes=event_duration,
                        number_of_meetings=events_count[event_duration])
                    for index, event_duration in enumerate(events_count)
                ]
                output = RoomStatistics(room_name=room_details[0]['roomName'],
                                        count=number_of_events_in_room,
                                        events=duration_of_events_in_room,
                                        has_events=True
                                        )
                result.append(output)
        return result

    def get_least_used_room_week(self, query, location_id, week_start, week_end):  # noqa: E501
        """ Get analytics for least used room per week
         :params
            - calendar_id, location_id
            - week_start, week_end(Time range)
        """
        week_start = RoomAnalytics.convert_date(self, week_start)
        week_end = RoomAnalytics.convert_date(self, week_end)

        rooms_available = RoomAnalytics.get_calendar_id_name(
            self, query, location_id)
        res = []
        number_of_least_events = float('inf')
        for room in rooms_available:
            calendar_events = RoomAnalytics.get_all_events_in_a_room(
                self, room['calendar_id'], week_start, week_end)
            output = []
            if not calendar_events:
                output.append({'RoomName': room['name'], 'has_events': False})
                number_of_least_events = 0
            for event in calendar_events:
                if event.get('attendees'):
                    event_details = RoomAnalytics.get_event_details(self, event, room['calendar_id'])  # noqa: E501
                    output.append(event_details)
            if len(output) < number_of_least_events:
                number_of_least_events = len(output)
            res.append(output)
        analytics = RoomAnalytics.get_room_statistics(
            self, number_of_least_events, res)
        return analytics

    def get_most_used_room_per_month(self, query, month, year, location_id):
        """ Get analytics for the most used room(s) per morth in a location
         :params
            - month, year, location_id
        """
        date = month + ' 1 ' + str(year)
        startdate = RoomAnalytics.convert_date(self, date)
        date_after_month = (datetime.strptime(date, '%b %d %Y') + relativedelta(months=1)).isoformat() + 'Z'  # noqa: E501

        rooms_available = RoomAnalytics.get_calendar_id_name(
            self, query, location_id)
        rooms = []
        res = []
        for room in rooms_available:
            calendar_events = RoomAnalytics.get_all_events_in_a_room(
                self, room['calendar_id'], startdate, date_after_month)
            output = []
            if not calendar_events:
                output.append({'RoomName': room['name'], 'has_events': False})
                rooms_with_max_events = 0
                rooms.append(rooms_with_max_events)

            else:
                for event in calendar_events:
                    if event.get('attendees'):
                        event_details = RoomAnalytics.get_event_details(
                            self, event, room['calendar_id'])
                        output.append(event_details)
                rooms.append(len(output))
            res.append(output)
        rooms_with_max_events = max(rooms)

        analytics = RoomAnalytics.get_room_statistics(
            self, rooms_with_max_events, res)
        return analytics
