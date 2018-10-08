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
    total_duration = graphene.Int()


class RoomAnalytics(Credentials):
    """Get room analytics
       :methods
           get_least_used_room_week
    """
    def convert_date(self, date):
        return datetime.strptime(date, '%b %d %Y').isoformat() + 'Z'

    def get_start_end_month_dates(self, month, year):
        date = month + ' 1 ' + str(year)
        start_date = RoomAnalytics.convert_date(self, date)
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

    def get_calendar_id_name(self, query, location_id):
        """ Get all room(name, calendar_id) in a location
         :params
            - location_id
        """
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

    def get_monthly_rooms_events(self, query, month, year, location_id):
        """ Get event stats for all rooms in a specified month
         :params
            - location_id, month, year
        """
        date = month + ' 1 ' + str(year)
        startdate = RoomAnalytics.convert_date(self, date)
        date_after_month = (datetime.strptime(date, '%b %d %Y') + relativedelta(months=1)).isoformat() + 'Z'  # noqa: E501

        rooms_available = RoomAnalytics.get_calendar_id_name(
            self, query, location_id)
        room_events_count = []
        events_in_all_rooms = []
        for room in rooms_available:
            calendar_events = RoomAnalytics.get_all_events_in_a_room(
                self, room['calendar_id'], startdate, date_after_month)
            output = []
            if not calendar_events:
                output.append({'RoomName': room['name'], 'has_events': False})
                room_with_no_events = 0
                room_events_count.append(room_with_no_events)

            else:
                for event in calendar_events:
                    if event.get('attendees'):
                        event_details = RoomAnalytics.get_event_details(
                            self, event, room['calendar_id'])
                        output.append(event_details)
                room_events_count.append(len(output))
            events_in_all_rooms.append(output)
        return dict(
            events_in_all_rooms=events_in_all_rooms,
            room_events_count=room_events_count
        )

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
        """ Get analytics for the MOST used room(s) per morth in a location
         :params
            - month, year, location_id
        """
        get_monthly_events = RoomAnalytics.get_monthly_rooms_events(
            self, query, month, year, location_id)
        rooms_with_max_events = max(get_monthly_events['room_events_count'])
        res = get_monthly_events['events_in_all_rooms']

        analytics = RoomAnalytics.get_room_statistics(
            self, rooms_with_max_events, res)
        return analytics

    def get_least_used_room_per_month(self, query, month, year, location_id):
        """ Get analytics for the LEAST used room(s) per morth in a location
         :params
            - month, year, location_id
        """
        get_monthly_events = RoomAnalytics.get_monthly_rooms_events(
            self, query, month, year, location_id)
        rooms_with_min_events = min(get_monthly_events['room_events_count'])
        res = get_monthly_events['events_in_all_rooms']

        analytics = RoomAnalytics.get_room_statistics(
            self, rooms_with_min_events, res)
        return analytics

    def get_meetings_per_room(self, query, location_id, timeMin, timeMax):
        day_start = RoomAnalytics.convert_date(self, timeMin)
        day_end = RoomAnalytics.convert_date(self, timeMax)
        rooms_available = RoomAnalytics.get_calendar_id_name(
            self, query, location_id)
        res = []
        for room in rooms_available:
            calendar_events = RoomAnalytics.get_all_events_in_a_room(
                self, room['calendar_id'], day_start, day_end)
            room_details = RoomStatistics(room_name=room["name"], count=len(calendar_events))  # noqa: E501
            res.append(room_details)
        return res

    def meetings_duration_statistics(self, query, location_id, start_date, end_date):  # noqa: E501
        """
        Get meeting durations statistics
        """
        rooms = RoomAnalytics.get_calendar_id_name(
            self, query, location_id)
        result = []
        for room in rooms:
            events = RoomAnalytics.get_all_events_in_a_room(self, room['calendar_id'], start_date, end_date)  # noqa: E501
            events_duration = []
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))  # noqa: E501
                end = event['end'].get('dateTime', event['end'].get('date'))
                duration = RoomAnalytics.get_time_duration_for_event(self, start, end)  # noqa: E501
                events_duration.append(duration)

            events_count = Counter(events_duration)

            events_in_minutes = [
                EventsDuration(
                    duration_in_minutes=events_duration,
                    number_of_meetings=events_count[events_duration])
                for index, events_duration in enumerate(events_count)
            ]

            output = RoomStatistics(
                room_name=room["name"],
                count=len(events_duration),
                total_duration=sum(events_duration),
                events=events_in_minutes
            )
            result.append(output)
        return result

    def get_most_used_room_week(self, query, location_id, week_start, week_end):  # noqa: E501
        """ Get analytics for most used room per week
         :params
            - calendar_id, location_id
            - week_start, week_end(Time range)
        """
        week_start = RoomAnalytics.convert_date(self, week_start)
        week_end = RoomAnalytics.convert_date(self, week_end)
        rooms_available = RoomAnalytics.get_calendar_id_name(
            self, query, location_id)
        res = []
        number_of_most_events = 0
        for room in rooms_available:
            calendar_events = RoomAnalytics.get_all_events_in_a_room(
                self, room['calendar_id'], week_start, week_end)
            output = []
            if not calendar_events:
                output.append({'RoomName': room['name'], 'has_events': False})
                number_of_most_events = 0
            else:
                for event in calendar_events:
                    event_details = RoomAnalytics.get_event_details(
                        self, event, room['calendar_id'])
                    output.append(event_details)
                if len(output) > number_of_most_events:
                    number_of_most_events = len(output)
            res.append(output)
        analytics = RoomAnalytics.get_room_statistics(
            self, number_of_most_events, res)
        return analytics

    def get_daily_meetings_details(self, query, location_id, day):  # noqa: E501
        """
        Get daily meetings durations details
        """
        start_date, day_after = RoomAnalytics.get_start_end_day_dates(self, day)  # noqa
        daily_analytics = RoomAnalytics.meetings_duration_statistics(self, query, location_id, start_date, day_after)  # noqa: E501
        return daily_analytics

    def get_meeting_duration_of_room_per_month(self, query, month, year, location_id):  # noqa
        """ Get analytics for thetotal meeting duration of room(s) per
        morth in a location
         :params
            - month, year, location_id
        """
        start_date, day_after = RoomAnalytics.get_start_end_month_dates(self, month, year)  # noqa
        monthly_analytics = RoomAnalytics.meetings_duration_statistics(self, query, location_id, start_date, day_after)  # noqa: E501
        return monthly_analytics
