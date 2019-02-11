import sys
import os
from tests.base import BaseTestCase, CommonTestCases
from fixtures.events.event_checkin_fixtures import (
    event_checkin_mutation,
    event_checkin_response,
    wrong_calendar_id_checkin_mutation,
    cancel_event_mutation,
    cancel_event_respone,
    checkin_mutation_for_event_existing_in_db,
    response_for_event_existing_in_db_checkin
)
from fixtures.events.events_ratios_fixtures import (
    event_ratio_percentage_cancellation_query,
    event_ratio_percentage_cancellation_response)

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

    def test_cancel_event(self):
        '''
        Test that event status is updated to cancelled.
        '''
        CommonTestCases.user_token_assert_equal(
            self,
            cancel_event_mutation,
            cancel_event_respone
        )

    def test_cancel_event_twice(self):
        '''
        test that you cannot cancel an event twice
        '''
        CommonTestCases.user_token_assert_equal(
            self,
            cancel_event_mutation,
            cancel_event_respone
        )
        CommonTestCases.user_token_assert_in(
            self,
            cancel_event_mutation,
            "Event already cancelled"
        )
        # Test for successful try in percentage_formater function
        CommonTestCases.admin_token_assert_equal(
            self,
            event_ratio_percentage_cancellation_query,
            event_ratio_percentage_cancellation_response
        )

    def test_check_in_to_a_cancelled_event(self):
        """
        test that you cannot check-in to a cancelled event
        """
        CommonTestCases.user_token_assert_equal(
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
