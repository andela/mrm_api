import sys
import os
from tests.base import BaseTestCase, CommonTestCases
from fixtures.events.event_checkin_fixtures import (
    event_checkin_mutation,
    event_checkin_response,
    wrong_calendar_id_checkin_mutation
)

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
            "This event already exists."
        )

    def test_checkin_with_invalid_calendar_id(self):
        """
        Test that an event can be checked into with correct details
        """
        CommonTestCases.user_token_assert_in(
            self,
            wrong_calendar_id_checkin_mutation,
            "This Calendar ID is not registered on Converge."
        )
