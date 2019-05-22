import graphene
import dateutil.parser
from graphql import GraphQLError
from utilities.utility import percentage_formater
from helpers.calendar.analytics_helper import CommonAnalytics


class Event(graphene.ObjectType):
    duration_in_minutes = graphene.Int()


class BookingsCount(graphene.ObjectType):
    period = graphene.String()
    bookings = graphene.Int()


class AllAnalyticsHelper:

    def bookings_count(self, unconverted_dates, events):
        """
        Get bookings count and period in a given room
        """
        start_date = unconverted_dates['start']
        day_after_end_date = unconverted_dates['end']
        bookings_count = []
        parsed_start_date = dateutil.parser.parse(start_date)
        parsed_end_date = dateutil.parser.parse(day_after_end_date)
        number_of_days = (parsed_end_date - parsed_start_date).days

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
                    bookings=bookings)
                bookings_count.append(output)
        else:
            dates = CommonAnalytics.get_list_of_month_dates(
                start_date,
                parsed_start_date,
                day_after_end_date,
                parsed_end_date)
            for date in dates:
                string_month = dateutil.parser.parse(date[0]).strftime("%B")
                bookings = 0
                for event in events:
                    if dateutil.parser.parse(event.start_time[:10]).strftime("%B") == string_month: # noqa
                        bookings += 1
                output = BookingsCount(
                    period=string_month,
                    bookings=bookings)
                bookings_count.append(output)

        return bookings_count

    def get_all_analytics(self, query, start_date, end_date, location_id, unconverted_dates): # noqa
        """
        Get all room analytics
        """
        rooms = query.filter_by(state="active", location_id=location_id).all()
        room_analytics = []
        bookings = 0
        for room in rooms:
            cancellations = 0
            checkins = 0
            events = []
            try:
                events_result = CommonAnalytics.get_all_events_in_a_room(
                    self, room.id, start_date, end_date)
            except GraphQLError:
                continue
            bookings_count = AllAnalyticsHelper.bookings_count(self, unconverted_dates, events_result) # noqa
            bookings += len(events_result)
            for event in events_result:
                if event.checked_in:
                    checkins += 1
                if event.cancelled:
                    cancellations += 1
                duaration_in_minutes = CommonAnalytics.get_time_duration_for_event(self, event.start_time, event.end_time) # noqa
                current_event = Event(
                    duration_in_minutes=duaration_in_minutes)
                events.append(current_event)
            room_analytic = {
                'number_of_meetings': len(events_result),
                'room_name': room.name,
                'cancellations': cancellations,
                'checkins': checkins,
                'cancellations_percentage': percentage_formater(cancellations, bookings), # noqa
                'checkins_percentage': percentage_formater(checkins, bookings),
                # TODO - work on app_bookings and autocancellation logic
                'app_bookings': cancellations,  # Place holder
                'app_bookings_percentage': percentage_formater(cancellations, bookings), # noqa
                'percentage_share': percentage_formater(
                    len(events_result), bookings
                ),
                'room_events': events,
                'bookings_count': bookings_count,
                'auto_cancellations': 0  # Placeholder
            }
            room_analytics.append(room_analytic)
            room_analytics.sort(key=lambda x: x['number_of_meetings'], reverse=True) # noqa
        return room_analytics, bookings
