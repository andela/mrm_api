from .credentials import Credentials
from helpers.calendar.analytics_helper import (CommonAnalytics)
from api.room.models import Room as RoomModel
from api.events.models import Events
from api.room.schema import CheckinsToBookingsRatio


class RoomAnalyticsRatios(Credentials):
    """Get room analytics ratios
       :methods
           get_least_used_room_week
    """

    def get_analytics_ratios(self, query, start, end):
        """ Get ratios of checkings to bookings of meeting rooms.
         :params
            - start_date, end_date
        """

        start_date, day_after_end_date = CommonAnalytics.convert_dates(
                self, start, end)
        rooms = CommonAnalytics.get_calendar_id_name(
            self, query)

        output = []
        checkins = 0
        for room in rooms:
            calendar_events = CommonAnalytics.get_all_events_in_a_room(
                self, room['calendar_id'], start_date, day_after_end_date)
            if calendar_events:
                for event in calendar_events:
                    if event.get('attendees'):
                        event_details = CommonAnalytics.get_event_details(
                            self, event, room['calendar_id'])
                        output.append(event_details)

            room_id = RoomModel.query.filter_by(calendar_id=room['calendar_id'],).first().id  # noqa
            checkins += (Events.query.filter(Events.room_id==room_id, Events.checked_in==True, Events.start_time>=start_date, Events.end_time<day_after_end_date)).count()  # noqa

        response = CheckinsToBookingsRatio(
                Checkins=checkins,
                Bookings=len(output)
                )
        return response
