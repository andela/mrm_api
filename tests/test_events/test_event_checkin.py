import sys
import os
from unittest.mock import patch
from tests.base import BaseTestCase, CommonTestCases
from fixtures.events.event_checkin_fixtures import (
    event_checkin_mutation,
    event_2_checkin_mutation,
    event_checkin_response,
    wrong_calendar_id_checkin_mutation,
    cancel_event_mutation,
    cancel_event_respone,
    cancel_event_invalid_start_time,
    checkin_mutation_for_event_existing_in_db,
    response_for_event_existing_in_db_checkin
)
from helpers.calendar.calendar import get_events_mock_data

sys.path.append(os.getcwd())


class TestEventCheckin(BaseTestCase):

    def test_checkin_to_event(self):
        """
        Test that an event can be checked into with correct details
        """
        CommonTestCases.user_token_assert_equal(
            self,
            event_checkin_mutation,
            event_checkin_response
        )

    def test_checkin_to_event_twice(self):
        """
        Test that you cant check into the same room twice
        """
        CommonTestCases.user_token_assert_equal(
            self,
            event_checkin_mutation,
            event_checkin_response
        )
        CommonTestCases.user_token_assert_in(
            self,
            event_checkin_mutation,
            "Event already checked in"
        )

    def test_checkin_with_invalid_calendar_id(self):
        """
        Test that an event can be checked into with correct details
        """
        CommonTestCases.user_token_assert_in(
            self,
            wrong_calendar_id_checkin_mutation,
            "This Calendar ID is invalid"
        )

    def test_checkin_room_with_no_device(self):
        """
        Test that user can not checkin to a room
        without a device assigned to the room
        """
        CommonTestCases.user_token_assert_in(
            self,
            event_2_checkin_mutation,
            "Room device not found"
        )

    @patch("api.events.schema.get_single_calendar_event", spec=True)
    def test_cancel_event(self, mocked_method):
        '''
        Test that event status is updated to cancelled.
        '''
        mocked_method.return_value = get_events_mock_data()['items'][0]
        CommonTestCases.user_token_assert_in(
            self,
            cancel_event_mutation,
            cancel_event_respone
        )

    @patch("api.events.schema.get_single_calendar_event", spec=True)
    def test_cancel_event_with_invalid_start_time(self, mocked_method):
        '''
        Test that user can not cancel event with invalid start time
        '''
        mocked_method.return_value = get_events_mock_data()['items'][0]
        CommonTestCases.user_token_assert_in(
            self,
            cancel_event_invalid_start_time,
            'Invalid start time'
        )

    @patch("api.events.schema.get_single_calendar_event", spec=True)
    def test_cancel_event_twice(self, mocked_method):
        '''
        test that you cannot cancel an event twice
        '''
        mocked_method.return_value = get_events_mock_data()['items'][0]
        CommonTestCases.user_token_assert_in(
            self,
            cancel_event_mutation,
            cancel_event_respone
        )
        CommonTestCases.user_token_assert_in(
            self,
            cancel_event_mutation,
            "Event already cancelled"
        )

    @patch("api.events.schema.get_single_calendar_event", spec=True)
    def test_check_in_to_a_cancelled_event(self, mocked_method):
        """
        test that you cannot check-in to a cancelled event
        """
        mocked_method.return_value = get_events_mock_data()['items'][0]
        CommonTestCases.user_token_assert_in(
            self,
            cancel_event_mutation,
            cancel_event_respone
        )
        CommonTestCases.user_token_assert_in(
            self,
            event_checkin_mutation,
            "Event already cancelled"
        )

    def test_cancel_a_checked_in_event(self):
        """
        test that you cannot check-in to a cancelled event
        """
        CommonTestCases.user_token_assert_equal(
            self,
            event_checkin_mutation,
            event_checkin_response
        )
        CommonTestCases.user_token_assert_in(
            self,
            cancel_event_mutation,
            "Event already checked in"
        )

    def test_check_in_event_existing_in_db(self):
        """
        test that you can check into an event that is already in the database
        """
        CommonTestCases.user_token_assert_equal(
            self,
            checkin_mutation_for_event_existing_in_db,
            response_for_event_existing_in_db_checkin
        )
