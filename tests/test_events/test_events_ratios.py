import sys
import os
from tests.base import BaseTestCase, CommonTestCases
from fixtures.events.events_ratios_fixtures import (
    event_ratio_query,
    event_ratio_response,
    event_ratio_for_one_day_query,
    event_ratio_per_room_query,
    event_ratio_per_room_response,
)

sys.path.append(os.getcwd())


class TestEventRatios(BaseTestCase):

    def test_events_checkins_to_bookings_ratio_on_date_range(self):
        """
        Test that an admin is able to get the ratio of checkins to bookings
        on a date range
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            event_ratio_query,
            event_ratio_response
        )

    def test_events_checkins_to_bookings_ratio_for_single_day(self):
        """
        Test that an admin is able to get the ratio of checkins to bookings
        with a single date supplied
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            event_ratio_for_one_day_query,
            event_ratio_response
        )

    def test_event_checkin_and_cancellation_ratio_per_room(self):
        """
        Test that an admin is able to get the ratio of checkins to bookings
        for each individual room
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            event_ratio_per_room_query,
            event_ratio_per_room_response
        )

    def test_database_connection_error(self):
        """
        test a user friendly message is returned to a user when database
        cannot be reached
        """
        BaseTestCase().tearDown()
        CommonTestCases.admin_token_assert_in(
            self,
            event_ratio_query,
            "The database cannot be reached"
        )
        CommonTestCases.admin_token_assert_in(
            self,
            event_ratio_for_one_day_query,
            "The database cannot be reached"
        )
        CommonTestCases.admin_token_assert_in(
            self,
            event_ratio_per_room_query,
            "The database cannot be reached"
        )
