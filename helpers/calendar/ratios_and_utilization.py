import dateutil.parser

from helpers.calendar.analytics_helper import (CommonAnalytics)
from api.room.models import Room as RoomModel
from api.events.models import Events
from api.room.schema import (RatioOfCheckinsAndCancellations,
                             BookingsAnalyticsCount)
from utilities.verify_ids_for_room import get_room_name


class RoomAnalyticsRatios:
    """Get room analytics ratios
       :methods
           get_least_used_room_week
    """

    def get_analytics_ratios(self, query, start, end):
        """ Get ratios of checkings/cancellations to bookings for all rooms.
         :params
            - start_date, end_date
        """
        start_date, day_after_end_date = CommonAnalytics.validate_current_date(
            self, start, end)
        rooms = CommonAnalytics.get_room_details(
            self, query)

        checkins = 0
        cancellations = 0
        calendar_events_list = []
        app_events_list = []

        for room in rooms:
            checkins, cancellations, calendar_events_list, app_events_list = RoomAnalyticsRatios().retrieve_cancellations_and_checkins_for_room(room['room_id'],  # noqa
                                                        start_date,
                                                        day_after_end_date,
                                                        checkins,
                                                        cancellations,
                                                        calendar_events_list,
                                                        app_events_list)

        ratio_object = RoomAnalyticsRatios().map_results_to_ratio_class(
            checkins=checkins,
            cancellations=cancellations,
            calendar_events_list=calendar_events_list,
            app_events_list=app_events_list)

        return ratio_object

    def get_analytics_ratios_per_room(self, query, start, end, **kwargs):
        """ Get ratios of checkings/cancellations to bookings per room.
         :params
            - start_date, end_date, room_id
        """
        room_id = kwargs.get('room_id')
        start_date, day_after_end_date = CommonAnalytics.validate_current_date(
            self, start, end)
        rooms = CommonAnalytics.get_room_details(
            self, query)

        response = []
        for room in rooms:
            checkins = 0
            cancellations = 0
            calendar_events_list = []
            app_events_list = []

            checkins, cancellations, calendar_events_list, app_events_list = RoomAnalyticsRatios().retrieve_cancellations_and_checkins_for_room(room['room_id'],  # noqa
                                                        start_date,
                                                        day_after_end_date,
                                                        checkins,
                                                        cancellations,
                                                        calendar_events_list,
                                                        app_events_list)

            ratio_object = RoomAnalyticsRatios().map_results_to_ratio_class(
                checkins=checkins,
                cancellations=cancellations,
                calendar_events_list=calendar_events_list,
                app_events_list=app_events_list,
                room_name=room['name'],
                room_id=room['room_id'])

            if room_id == ratio_object.room_id:
                return ratio_object

            response.append(ratio_object)

        return response

    def retrieve_cancellations_and_checkins_for_room(self,
                                                     room_id,
                                                     start_date,
                                                     day_after_end_date,
                                                     checkins,
                                                     cancellations,
                                                     calendar_events_list,
                                                     app_events_list):
        """ Retrieve cancellations and checkins for a room
        :params
            - room_id, start_date, day_after_end_date,
                checkins,cancellations, output
        """
        all_events = CommonAnalytics.get_all_events_in_a_room(
            self, room_id, start_date, day_after_end_date)
        if all_events:
            for event in all_events:
                if event.number_of_participants:
                    calendar_events_list.append(event)
        room_id = RoomModel.query.filter_by(id=room_id).first().id

        checkins += (Events.query.filter(Events.room_id == room_id, Events.checked_in == True, Events.start_time >= start_date, Events.end_time < day_after_end_date)).count()  # noqa

        cancellations += (Events.query.filter(Events.room_id == room_id, Events.cancelled == True, Events.start_time >= start_date, Events.end_time < day_after_end_date)).count()  # noqa

        return checkins, cancellations, calendar_events_list, app_events_list

    def map_results_to_ratio_class(self, **kwargs):
        """ Maps the checkins and cancellations to the ratio object
        :params
            - checkins, cancellations, calendar_events_list, app_events_list,
            room_name, room_id
        """
        checkins = kwargs.get('checkins')
        cancellations = kwargs.get('cancellations')
        app_events_list = kwargs.get('app_events_list')

        bookings = len(kwargs.get('calendar_events_list')) + len(
            app_events_list) + cancellations
        app_bookings = len(app_events_list) + cancellations
        app_bookings_percentage = RoomAnalyticsRatios().percentage_formater(
            app_bookings,
            bookings)
        cancellations_percentage = RoomAnalyticsRatios().percentage_formater(
            cancellations,
            bookings)
        checkins_percentage = RoomAnalyticsRatios().percentage_formater(
            checkins,
            bookings)
        result = RatioOfCheckinsAndCancellations(
            room_id=kwargs.get('room_id'),
            room_name=kwargs.get('room_name'),
            checkins=checkins,
            cancellations=cancellations,
            bookings=bookings,
            checkins_percentage=checkins_percentage,
            cancellations_percentage=cancellations_percentage,
            app_bookings=app_bookings,
            app_bookings_percentage=app_bookings_percentage,
        )
        return result

    def percentage_formater(self, portion, total):
        """ Calculates the percentage of the entered portion to the total and returns it
         :params
            - portion, total
        """
        try:
            percentage = (portion/total) * 100
            return percentage
        except ZeroDivisionError:
            return 0

    def get_bookings_analytics_count(self, query, start, end, room_id=None):
        results = []
        start_date, day_after_end_date = CommonAnalytics.convert_dates(
            self, start, end)
        start_dt = dateutil.parser.parse(start_date)
        end_dt = dateutil.parser.parse(day_after_end_date)
        number_of_days = (end_dt - start_dt).days
        room_name = get_room_name(room_id)

        if number_of_days <= 30:
            dates = CommonAnalytics.get_list_of_dates(
                start, number_of_days)
            for date in dates:
                bookings = CommonAnalytics.get_total_bookings(
                    self, query, date[0], date[1], room_id=room_id)
                string_date = dateutil.parser.parse(
                    date[0]).strftime("%b %d %Y")
                output = BookingsAnalyticsCount(
                    period=string_date, bookings=bookings, room_name=room_name)
                results.append(output)

        else:
            dates = CommonAnalytics.get_list_of_month_dates(
                start_date, start_dt, day_after_end_date, end_dt)
            for date in dates:
                bookings = CommonAnalytics.get_total_bookings(
                    self, query, date[0], date[1], room_id=room_id)
                string_month = dateutil.parser.parse(date[0]).strftime("%B")
                output = BookingsAnalyticsCount(
                    period=string_month, bookings=bookings, room_name=room_name)
                results.append(output)

        return results
