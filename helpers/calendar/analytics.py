from collections import Counter
from helpers.calendar.analytics_helper import (
    CommonAnalytics, EventsDuration, RoomStatistics
)


class RoomAnalytics:
    """Get room analytics
       :methods
           get_events_number_meetings_room_analytics
           get_meetings_per_room_analytics
           get_meetings_duration_analytics
    """

    def get_events_number_meetings_room_analytics(self, query, start_date, end_date):  # noqa: E501
        """ Get events in rooms and number of meetings per room
         :params
            - query
            - start_date, end_date(Time range)
        """
        start_date, end_date = CommonAnalytics.convert_dates(
            self, start_date, end_date)
        rooms_available = CommonAnalytics.get_room_details(
            self, query)
        result, number_of_meetings = [], []
        for room in rooms_available:
            all_events = CommonAnalytics.get_all_events_in_a_room(
                self, room['room_id'], start_date, end_date)
            output = []
            if not all_events:
                output.append({'roomName': room['name']})
                number_of_meetings.append(0)
            else:
                for event in all_events:
                    if event.number_of_participants:
                        event_details = CommonAnalytics.get_event_details(
                            self, query, event, room['room_id'])
                        output.append(event_details)
                number_of_meetings.append(len(output))
            result.append(output)
        return (result, number_of_meetings)

    def get_meetings_per_room_analytics(self, query, start_date, end_date):
        """ Get analytics for meetings per room
         :params
            - query
            - start_date, end_date(Time range)
        """
        start_date, end_date = CommonAnalytics.convert_dates(
            self, start_date, end_date)
        rooms_available = CommonAnalytics.get_room_details(
            self, query)
        res = []
        for room in rooms_available:
            all_events = CommonAnalytics.get_all_events_in_a_room(
                self, room['room_id'], start_date, end_date)
            room_details = RoomStatistics(room_name=room["name"], count=len(all_events))  # noqa: E501
            res.append(room_details)
        return res

    def get_meetings_duration_analytics(self, query, start_date, end_date):  # noqa: E501
        """ Get analytics for meetings durations in rooms
         :params
            - query
            - start_date, end_date(Time range)
        """
        start_date, end_date = CommonAnalytics.validate_current_date(
            self, start_date, end_date)
        rooms = CommonAnalytics.get_room_details(
            self, query)
        result = []
        for room in rooms:
            events = CommonAnalytics.get_all_events_in_a_room(
                self, room['room_id'], start_date, end_date)
            events_duration = []
            for event in events:
                start = event.start_time
                end = event.end_time
                duration = CommonAnalytics.get_time_duration_for_event(self, start, end)  # noqa: E501
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

    def get_booked_rooms(self, query, start_date, end_date):  # noqa: E501
        """ Get booked room per given period of time and their percentages
         :params
            - query
            - start_date, end_date(Time range)
        """
        start_date, end_date = CommonAnalytics.convert_dates(
            self, start_date, end_date)
        rooms_available = CommonAnalytics.get_room_details(
            self, query)
        result = []
        bookings = 0
        for room in rooms_available:
            all_events_in_all_rooms = CommonAnalytics.get_all_events_in_a_room(
                self, room['room_id'], start_date, end_date)
            if all_events_in_all_rooms:
                bookings += len(all_events_in_all_rooms)

        for room in rooms_available:
            all_events = CommonAnalytics.get_all_events_in_a_room(
                self, room['room_id'], start_date, end_date)
            if all_events:
                room_details = RoomStatistics(
                    room_name=room["name"],
                    meetings=len(all_events),
                    percentage=(len(all_events))/bookings*100)

                result.append(room_details)
                result.sort(key=lambda x: x.meetings, reverse=True)
            else:
                return result
        return result
