import graphene
from datetime import datetime
import dateutil.parser
from dateutil.relativedelta import relativedelta
from graphql import GraphQLError
from collections import Counter
from api.location.models import Location as LocationModel
from helpers.room_filter.room_filter import room_join_location
from helpers.auth.admin_roles import admin_roles
from .credentials import Credentials


class EventsDuration(graphene.ObjectType):
    duration_in_minutes = graphene.Int()
    number_of_meetings = graphene.Int()


class RoomStatistics(graphene.ObjectType):
    room_name = graphene.String()
    count = graphene.Int()
    events = graphene.List(EventsDuration)
    has_events = graphene.Boolean()
    total_duration = graphene.Int()


class CommonAnalytics(Credentials):

    def convert_date(self, date):
        return datetime.strptime(date, '%b %d %Y').isoformat() + 'Z'

    def get_start_end_month_dates(self, month, year):
        date = month + ' 1 ' + str(year)
        start_date = CommonAnalytics.convert_date(self, date)
        day_after = (datetime.strptime(date, '%b %d %Y') + relativedelta(months=1)).isoformat() + 'Z'  # noqa: E501
        return(start_date, day_after)

    def get_start_end_day_dates(self, day):
        """
        Returns start and end day dates in iso-format
        """
        start = (datetime.strptime(day, "%b %d %Y"))
        startdate = start.isoformat() + 'Z'
        end = (start + relativedelta(days=1)).isoformat() + 'Z'
        return(startdate, end)

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

    def get_calendar_id_name(self, query):
        """ Get all room(name, calendar_id) in a location
         :params
        """
        location_id = admin_roles.admin_location_for_analytics_view()
        exact_query = room_join_location(query)
        rooms_in_locations = exact_query.filter(
            LocationModel.id == location_id)
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
                    event_details["minutes"] = CommonAnalytics.get_time_duration_for_event(  # noqa: E501
                        self,
                        event['start'].get('dateTime', event['start'].get('date')),  # noqa: E501
                        event['end'].get('dateTime', event['end'].get('date'))
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
                events_count = Counter(
                    detail['minutes'] for detail in room_details if detail)
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
