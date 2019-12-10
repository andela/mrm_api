import graphene
import pytz
import dateutil.parser
from graphql import GraphQLError
from datetime import datetime
from dateutil.relativedelta import relativedelta
from helpers.calendar.analytics_helper import CommonAnalytics
from utilities.utility import percentage_formater


class Event(graphene.ObjectType):
    duration_in_minutes = graphene.Int()


class BookingsCount(graphene.ObjectType):
    period = graphene.String()
    total_bookings = graphene.Int()


class DeviceAnalytics(graphene.ObjectType):
    device_name = graphene.String()
    device_id = graphene.Int()
    down_time = graphene.String()


class AllAnalyticsHelper:
    def count_bookings_within_period(events, date_pattern, string_date):
        """
        Counts the bookings within a specified period
        """
        user_time_zone = CommonAnalytics.get_user_time_zone()
        bookings = 0
        for event in events:
            start_timez = dateutil.parser.parse(event.start_time).astimezone(
                pytz.timezone(user_time_zone)
            )  # noqa
            if start_timez.strftime(date_pattern) == string_date:
                bookings += 1
        return bookings

    def map_bookings_to_period(dates, date_pattern, events):
        """
        Maps bookings to the period in which they occurred
        """
        bookings_count = []
        for date in dates:
            string_date = dateutil.parser.parse(date[0]).strftime(date_pattern)
            bookings = AllAnalyticsHelper.count_bookings_within_period(
                events, date_pattern, string_date
            )
            output = BookingsCount(period=string_date, total_bookings=bookings)
            bookings_count.append(output)
        return bookings_count

    def bookings_count(self, unconverted_dates, events):
        """
        Get bookings count and period in a given room
        """
        start_date = unconverted_dates["start"]
        day_after_end_date = unconverted_dates["end"]
        parsed_start_date = dateutil.parser.parse(start_date)
        parsed_end_date = dateutil.parser.parse(day_after_end_date)
        parsed_day_after_end_date = parsed_end_date + relativedelta(days=1)
        number_of_days = (parsed_day_after_end_date - parsed_start_date).days
        dates = []
        date_pattern = "%b %d %Y"
        if number_of_days <= 30:
            dates = CommonAnalytics.get_list_of_dates(
                start_date, number_of_days)
        else:
            dates = CommonAnalytics.get_list_of_month_dates(
                start_date,
                parsed_start_date,
                day_after_end_date,
                parsed_day_after_end_date,
            )
            date_pattern = "%b %Y"

        return AllAnalyticsHelper.map_bookings_to_period(
            dates, date_pattern, events)

    def get_events_statistics(self, events):
        """
        Gets total checkins, app_bookings... from events
        """
        events_stats = {
            "checkins": 0,
            "app_bookings": 0,
            "auto_cancellations": 0,
            "cancellations": 0,
            "duration_in_minutes": 0,
        }
        for event in events:
            events_stats["checkins"] += bool(event.checked_in)
            events_stats["app_bookings"] += bool(event.app_booking)
            events_stats["auto_cancellations"] += bool(event.auto_cancelled)
            events_stats["cancellations"] += bool(event.cancelled)
            events_stats[
                "duration_in_minutes"
            ] += CommonAnalytics.get_time_duration_for_event(  # noqa
                self, event.start_time, event.end_time
            )
        return events_stats

    def convert_to_human_readable(date_time):
        """
        converts a datetime object to the
        format "X days, Y hours ago"

        @param date_time: datetime object

        @return:
            Human readable date time
        """
        user_time_zone = CommonAnalytics.get_user_time_zone()
        local_time = datetime.now().astimezone(
            pytz.timezone(user_time_zone)
        )
        date_now = local_time.strftime("%Y-%m-%d %H:%M:%S")
        current_time = datetime.strptime(str(date_now), "%Y-%m-%d %H:%M:%S")
        last_seen = datetime.strptime(str(date_time), "%Y-%m-%d %H:%M:%S")
        difference = relativedelta(current_time, last_seen)
        years = difference.years
        months = difference.months
        days = difference.days
        hours = difference.hours
        minutes = difference.minutes
        result = {
            "years": years,
            "months": months,
            "days": days,
            "hours": hours,
            "minutes": minutes,
        }
        date = []
        for key, value in result.items():
            if value > 0:
                date_string = str(value) + " " + key
                date.append(date_string)

        return ", ".join(date) + " ago."

    def get_devices_analytics(self, query):
        """
        Get devices str(diff.months) + analytic
        """
        devices = query.filter_by(state="active").all()
        device_analytics = []
        for device in devices:
            down_time = AllAnalyticsHelper.convert_to_human_readable(
                device.last_seen)
            device_obj = {
                "device_name": device.name,
                "device_id": device.id,
                "down_time": "this device was seen {}".format(down_time),
            }
            device_analytics.append(device_obj)

        return device_analytics

    def get_all_analytics(self, query, **kwargs):
        """
        Get all room analytics
        """
        start_date = kwargs["start_date"]
        end_date = kwargs["end_date"]
        location_id = kwargs["location_id"]
        unconverted_dates = kwargs["unconverted_dates"]
        rooms = query.filter_by(state="active", location_id=location_id).all()
        room_analytics = []
        bookings = 0
        total_checkins = 0
        total_app_bookings = 0
        total_auto_cancellations = 0
        total_cancellations = 0
        bookings_count = []
        all_events = []
        for room in rooms:
            events = []
            try:
                events_result = CommonAnalytics.get_all_events_in_a_room(
                    self, room.id, start_date, end_date
                )
            except GraphQLError:
                continue
            all_events += events_result
            bookings += len(events_result)
            events_stats = AllAnalyticsHelper.get_events_statistics(
                self, events_result
            )  # noqa
            current_event = Event(
                duration_in_minutes=events_stats["duration_in_minutes"]
            )
            events.append(current_event)
            total_checkins += events_stats["checkins"]
            total_app_bookings += events_stats["app_bookings"]
            total_auto_cancellations += events_stats["auto_cancellations"]
            total_cancellations += events_stats["cancellations"]
            num_of_events = len(events_result)
            room_analytic = {
                "number_of_meetings": num_of_events,
                "room_name": room.name,
                "num_of_events": num_of_events,
                "room_events": events,
                "cancellations": events_stats["cancellations"],
                "checkins": events_stats["checkins"],
                "auto_cancellations": events_stats["auto_cancellations"],
                "cancellations_percentage": percentage_formater(
                    events_stats["cancellations"], num_of_events
                ),
                "checkins_percentage": percentage_formater(
                    events_stats["checkins"], num_of_events
                ),
                "app_bookings": events_stats["app_bookings"],
                "app_bookings_percentage": percentage_formater(
                    events_stats["app_bookings"], num_of_events
                ),  # noqa
            }
            room_analytics.append(room_analytic)
            room_analytics.sort(
                key=lambda x: x["number_of_meetings"], reverse=True
            )  # noqa
        percentages_dict = {
            "total_checkins": total_checkins,
            "total_auto_cancellations": total_auto_cancellations,
            "total_app_bookings": total_app_bookings,
            "total_cancellations": total_cancellations,
        }
        bookings_count += AllAnalyticsHelper.bookings_count(
            self, unconverted_dates, all_events
        )  # noqa
        return room_analytics, bookings, percentages_dict, bookings_count
