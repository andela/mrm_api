from datetime import datetime
from dateutil.relativedelta import relativedelta
from collections import Counter
from .credentials import Credentials
from helpers.calendar.analytics_helper import (
    CommonAnalytics, EventsDuration, RoomStatistics
    )


class RoomAnalytics(Credentials):
    """Get room analytics
       :methods
           get_least_used_room_week
    """
    def get_monthly_rooms_events(self, query, month, year):
        """ Get event stats for all rooms in a specified month
         :params
            - month, year
        """
        date = month + ' 1 ' + str(year)
        startdate = CommonAnalytics.convert_date(self, date)
        date_after_month = (datetime.strptime(date, '%b %d %Y') + relativedelta(months=1)).isoformat() + 'Z'  # noqa: E501

        rooms_available = CommonAnalytics.get_calendar_id_name(
            self, query)
        room_events_count = []
        events_in_all_rooms = []
        for room in rooms_available:
            calendar_events = CommonAnalytics.get_all_events_in_a_room(
                self, room['calendar_id'], startdate, date_after_month)
            output = []
            if not calendar_events:
                output.append({'RoomName': room['name'], 'has_events': False})
                room_with_no_events = 0
                room_events_count.append(room_with_no_events)

            else:
                for event in calendar_events:
                    if event.get('attendees'):
                        event_details = CommonAnalytics.get_event_details(
                            self, event, room['calendar_id'])
                        output.append(event_details)
                room_events_count.append(len(output))
            events_in_all_rooms.append(output)
        return dict(
            events_in_all_rooms=events_in_all_rooms,
            room_events_count=room_events_count
        )

    def get_least_used_rooms(self, rooms_available, time_start, time_end):

        res = []
        number_of_least_events = float('inf')
        for room in rooms_available:
            calendar_events = CommonAnalytics.get_all_events_in_a_room(
                self, room['calendar_id'], time_start, time_end)
            output = []
            if not calendar_events:
                output.append({'RoomName': room['name'], 'has_events': False})
                number_of_least_events = 0
            for event in calendar_events:
                if event.get('attendees'):
                    event_details = CommonAnalytics.get_event_details(self, event, room['calendar_id'])  # noqa: E501
                    output.append(event_details)
            if len(output) < number_of_least_events:
                number_of_least_events = len(output)
            res.append(output)
        analytics = CommonAnalytics.get_room_statistics(
            self, number_of_least_events, res)
        return analytics

    def get_least_used_room_day(self, query, day):
        """ Get event stats for all rooms in a specified day
            :params
                - day
        """
        day_start, day_end = CommonAnalytics.get_start_end_day_dates(self, day)
        rooms_available = CommonAnalytics.get_calendar_id_name(
            self, query)
        return RoomAnalytics.get_least_used_rooms(self, rooms_available, day_start, day_end)  # noqa: E501

    def get_least_used_room_week(self, query, week_start, week_end):  # noqa: E501
        """ Get analytics for least used room per week
         :params
            - calendar_id
            - week_start, week_end(Time range)
        """
        week_start = CommonAnalytics.convert_date(self, week_start)
        week_end = CommonAnalytics.convert_date(self, week_end)

        rooms_available = CommonAnalytics.get_calendar_id_name(
            self, query)
        return RoomAnalytics.get_least_used_rooms(self, rooms_available, week_start, week_end)  # noqa: E501

    def get_most_used_room_per_month(self, query, month, year):
        """ Get analytics for the MOST used room(s) per morth in a location
         :params
            - month, year
        """
        get_monthly_events = RoomAnalytics.get_monthly_rooms_events(
            self, query, month, year)
        rooms_with_max_events = max(get_monthly_events['room_events_count'])
        res = get_monthly_events['events_in_all_rooms']

        analytics = CommonAnalytics.get_room_statistics(
            self, rooms_with_max_events, res)
        return analytics

    def get_least_used_room_per_month(self, query, month, year):
        """ Get analytics for the LEAST used room(s) per morth in a location
         :params
            - month, year
        """
        get_monthly_events = RoomAnalytics.get_monthly_rooms_events(
            self, query, month, year)
        rooms_with_min_events = min(get_monthly_events['room_events_count'])
        res = get_monthly_events['events_in_all_rooms']

        analytics = CommonAnalytics.get_room_statistics(
            self, rooms_with_min_events, res)
        return analytics

    def get_meetings_per_room(self, query, timeMin, timeMax):
        day_start = CommonAnalytics.convert_date(self, timeMin)
        day_end = CommonAnalytics.convert_date(self, timeMax)
        rooms_available = CommonAnalytics.get_calendar_id_name(
            self, query)
        res = []
        for room in rooms_available:
            calendar_events = CommonAnalytics.get_all_events_in_a_room(
                self, room['calendar_id'], day_start, day_end)
            room_details = RoomStatistics(room_name=room["name"], count=len(calendar_events))  # noqa: E501
            res.append(room_details)
        return res

    def meetings_duration_statistics(self, query, start_date, end_date):  # noqa: E501
        """
        Get meeting durations statistics
        """
        rooms = CommonAnalytics.get_calendar_id_name(
            self, query)
        result = []
        for room in rooms:
            events = CommonAnalytics.get_all_events_in_a_room(self, room['calendar_id'], start_date, end_date)  # noqa: E501
            events_duration = []
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))  # noqa: E501
                end = event['end'].get('dateTime', event['end'].get('date'))
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

    def get_most_used_room_week(self, query, week_start, week_end):  # noqa: E501
        """ Get analytics for most used room per week
         :params
            - calendar_id
            - week_start, week_end(Time range)
        """
        week_start = CommonAnalytics.convert_date(self, week_start)
        week_end = CommonAnalytics.convert_date(self, week_end)
        rooms_available = CommonAnalytics.get_calendar_id_name(
            self, query)
        res = []
        number_of_most_events = 0
        for room in rooms_available:
            calendar_events = CommonAnalytics.get_all_events_in_a_room(
                self, room['calendar_id'], week_start, week_end)
            output = []
            if not calendar_events:
                output.append({'RoomName': room['name'], 'has_events': False})
                number_of_most_events = 0
            else:
                for event in calendar_events:
                    event_details = CommonAnalytics.get_event_details(
                        self, event, room['calendar_id'])
                    output.append(event_details)
                if len(output) > number_of_most_events:
                    number_of_most_events = len(output)
            res.append(output)
        analytics = CommonAnalytics.get_room_statistics(
            self, number_of_most_events, res)
        return analytics

    def get_daily_meetings_details(self, query, day):  # noqa: E501
        """
        Get daily meetings durations details
        """
        start_date, day_after = CommonAnalytics.get_start_end_day_dates(self, day)  # noqa
        daily_analytics = RoomAnalytics.meetings_duration_statistics(self, query, start_date, day_after)  # noqa: E501
        return daily_analytics

    def get_meeting_duration_of_room_per_month(self, query, month, year):  # noqa
        """ Get analytics for thetotal meeting duration of room(s) per
        morth in a location
         :params
            - month, year
        """
        start_date, day_after = CommonAnalytics.get_start_end_month_dates(self, month, year)  # noqa
        monthly_analytics = RoomAnalytics.meetings_duration_statistics(self, query, start_date, day_after)  # noqa: E501
        return monthly_analytics

    def get_weekly_meetings_details(self, query, week_start, week_end):  # noqa: E501
        """
        Get weekly meeting durations details
        """
        week_start = CommonAnalytics.convert_date(self, week_start)
        week_end, day_after = CommonAnalytics.get_start_end_day_dates(self, week_end)  # noqa: E501
        weekly_analytics = RoomAnalytics.meetings_duration_statistics(self, query, week_start, day_after)  # noqa: E501
        return weekly_analytics
