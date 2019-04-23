import sys
import os

from tests.base import BaseTestCase, CommonTestCases
from fixtures.events.events_ratios_fixtures import (
    event_ratio_query,
    event_ratio_response,
    event_ratio_for_one_day_query,
    event_ratio_per_room_query,
    event_ratio_per_room_response,
    event_ratio_single_room_query,
    event_ratio_single_room_response,
    event_ratio_single_room_query_with_non_existing_id,
    event_ratio_single_room_with_non_existing_id_response
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

    def test_event_checkin_and_cancellation_single_room(self):
        """
        Test that an admin is able to get the ratio of checkins to bookings
        for a single room
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            event_ratio_single_room_query,
            event_ratio_single_room_response
        )

    def test_event_checkin_cancellation_single_room_wrong_id(self):
        """
        Tests that an admin cannot get the ratio of check-ins to bookings for a
        single room with invalid room id
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            event_ratio_single_room_query_with_non_existing_id,
            event_ratio_single_room_with_non_existing_id_response
        )
