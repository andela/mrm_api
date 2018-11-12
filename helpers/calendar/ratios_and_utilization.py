from .credentials import Credentials
from helpers.calendar.analytics_helper import (CommonAnalytics)
from api.room.models import Room as RoomModel
from api.events.models import Events
from api.room.schema import RatioOfCheckinsAndCancellations


class RoomAnalyticsRatios(Credentials):
    """Get room analytics ratios
       :methods
           get_least_used_room_week
    """

    def get_analytics_ratios(self, query, start, end):
        """ Get ratios of checkings/cancellations to bookings for all rooms.
         :params
            - start_date, end_date
        """
        start_date, day_after_end_date = CommonAnalytics.convert_dates(
                self, start, end)
        rooms = CommonAnalytics.get_calendar_id_name(
            self, query)

        checkins = 0
        events_list = []
        cancellations = 0

        for room in rooms:
            checkins, cancellations, events_list = RoomAnalyticsRatios.retrieve_cancellations_and_checkins_for_room(self,  # noqa
                                                        room['calendar_id'],
                                                        start_date,
                                                        day_after_end_date,
                                                        checkins,
                                                        cancellations,
                                                        events_list)

        ratio_object = RoomAnalyticsRatios.map_results_to_ratio_class(self,  # noqa
                            checkins,
                            cancellations,
                            events_list)

        return ratio_object

    def get_analytics_ratios_per_room(self, query, start, end):
        """ Get ratios of checkings/cancellations to bookings per room.
         :params
            - start_date, end_date
        """
        start_date, day_after_end_date = CommonAnalytics.convert_dates(
                self, start, end)
        rooms = CommonAnalytics.get_calendar_id_name(
            self, query)

        response = []
        for room in rooms:
            events_list = []
            checkins = 0
            cancellations = 0

            checkins, cancellations, events_list = RoomAnalyticsRatios.retrieve_cancellations_and_checkins_for_room(self,  # noqa
                                                        room['calendar_id'],
                                                        start_date,
                                                        day_after_end_date,
                                                        checkins,
                                                        cancellations,
                                                        events_list)

            ratio_object = RoomAnalyticsRatios.map_results_to_ratio_class(self,  # noqa
                                checkins,
                                cancellations,
                                events_list,
                                room['name'])

            response.append(ratio_object)
        return response

    def retrieve_cancellations_and_checkins_for_room(self, calendar_id, start_date, day_after_end_date, checkins,cancellations, events_list):  # noqa
        """ Retrieve cancellations and checkins for a room
        :params
            - calendar_id, start_date, day_after_end_date,
                checkins,cancellations, output
        """
        calendar_events = CommonAnalytics.get_all_events_in_a_room(
                self, calendar_id, start_date, day_after_end_date)
        if calendar_events:
            for event in calendar_events:
                if event.get('attendees'):
                    event_details = CommonAnalytics.get_event_details(
                        self, event, calendar_id)
                    events_list.append(event_details)

        room_id = RoomModel.query.filter_by(calendar_id=calendar_id,).first().id  # noqa

        checkins += (Events.query.filter(Events.room_id==room_id, Events.checked_in==True, Events.start_time>=start_date, Events.end_time<day_after_end_date)).count()  # noqa

        cancellations += (Events.query.filter(Events.room_id==room_id, Events.cancelled==True, Events.start_time>=start_date, Events.end_time<day_after_end_date)).count()  # noqa

        return checkins, cancellations, events_list

    def map_results_to_ratio_class(self, checkins, cancellations, events_list, room_name=None):  # noqa
        """ Maps the checkins and cancellations to the ratio object
        :params
            - checkins, cancellations, output, room_name
        """
        bookings = len(events_list) + cancellations
        cancellations_percentage = RoomAnalyticsRatios.percentage_formater(
            cancellations,
            bookings)
        checkins_percentage = RoomAnalyticsRatios.percentage_formater(
            checkins,
            bookings)
        result = RatioOfCheckinsAndCancellations(
                room_name=room_name,
                checkins=checkins,
                cancellations=cancellations,
                bookings=bookings,
                checkins_percentage=checkins_percentage,
                cancellations_percentage=cancellations_percentage
            )
        return result

    def percentage_formater(portion, total):
        """ Calculates the percentage of the entered portion to the total and returns it
         :params
            - portion, total
        """
        try:
            percentage = (portion/total) * 100
            return round(percentage, 1)
        except ZeroDivisionError:
            return 0
