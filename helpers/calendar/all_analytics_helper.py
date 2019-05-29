import graphene
import dateutil.parser
from graphql import GraphQLError
from helpers.calendar.analytics_helper import CommonAnalytics
from utilities.utility import percentage_formater
from dateutil.relativedelta import relativedelta


class Event(graphene.ObjectType):
    duration_in_minutes = graphene.Int()


class BookingsCount(graphene.ObjectType):
    period = graphene.String()
    total_bookings = graphene.Int()


class AllAnalyticsHelper:

    def bookings_count(self, unconverted_dates, events):
        """
        Get bookings count and period in a given room
        """
        start_date = unconverted_dates['start']
        day_after_end_date = unconverted_dates['end']
        parsed_start_date = dateutil.parser.parse(start_date)
        parsed_end_date = dateutil.parser.parse(day_after_end_date)
        parsed_day_after_end_date = parsed_end_date + relativedelta(days=1)
        number_of_days = (parsed_day_after_end_date - parsed_start_date).days
        bookings_count = []
        if number_of_days <= 30:
            dates = CommonAnalytics.get_list_of_dates(
                start_date, number_of_days)
            for date in dates:
                bookings = 0
                string_date = dateutil.parser.parse(
                    date[0]).strftime("%b %d %Y")
                for event in events:
                    if dateutil.parser.parse(event.start_time[:10]).strftime("%b %d %Y") == string_date: # noqa
                        bookings += 1
                output = BookingsCount(
                    period=string_date,
                    total_bookings=bookings)
                bookings_count.append(output)
        else:
            dates = CommonAnalytics.get_list_of_month_dates(
                start_date,
                parsed_start_date,
                day_after_end_date,
                parsed_day_after_end_date)
            for date in dates:
                string_month = dateutil.parser.parse(date[0]).strftime("%b %Y")
                output = BookingsCount(
                    period=string_month,
                    total_bookings=0)
                for event in events:
                    if dateutil.parser.parse(event.start_time[:10]).strftime("%b %Y") == string_month: # noqa
                        output.total_bookings += 1
                bookings_count.append(output)
        return bookings_count

    def get_all_analytics(self, query, start_date, end_date, location_id, unconverted_dates): # noqa
        """
        Get all room analytics
        """
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
            duaration_in_minutes = 0
            cancellations = 0
            checkins = 0
            auto_cancellations = 0
            app_bookings = 0
            try:
                events_result = CommonAnalytics.get_all_events_in_a_room(
                    self, room.id, start_date, end_date)
            except GraphQLError:
                continue
            all_events += events_result
            bookings += len(events_result)
            for event in events_result:
                if event.checked_in:
                    checkins += 1
                if event.app_booking:
                    app_bookings += 1
                if event.auto_cancelled:
                    auto_cancellations += 1
                if event.cancelled:
                    cancellations += 1
                duaration_in_minutes += CommonAnalytics.get_time_duration_for_event( # noqa
                    self, event.start_time, event.end_time
                )
            current_event = Event(
                duration_in_minutes=duaration_in_minutes)
            events.append(current_event)
            total_checkins += checkins
            total_app_bookings += app_bookings
            total_auto_cancellations += auto_cancellations
            total_cancellations += cancellations
            num_of_events = len(events_result)
            room_analytic = {
                'number_of_meetings': num_of_events,
                'room_name': room.name,
                'num_of_events': num_of_events,
                'room_events': events,
                'cancellations': cancellations,
                'checkins': checkins,
                'auto_cancellations': auto_cancellations,
                'cancellations_percentage': percentage_formater(
                    cancellations, num_of_events
                ),
                'checkins_percentage': percentage_formater(
                    checkins, num_of_events
                ),
                'app_bookings': app_bookings,
                'app_bookings_percentage': percentage_formater(app_bookings, num_of_events) # noqa
            }
            room_analytics.append(room_analytic)
            room_analytics.sort(key=lambda x: x['number_of_meetings'], reverse=True) # noqa
        percentages_dict = {
            'total_checkins': total_checkins,
            'total_auto_cancellations': total_auto_cancellations,
            'total_app_bookings': total_app_bookings,
            'total_cancellations': total_cancellations
        }
        bookings_count += AllAnalyticsHelper.bookings_count(self, unconverted_dates, all_events) # noqa
        return room_analytics, bookings, percentages_dict, bookings_count
