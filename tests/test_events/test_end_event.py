from tests.base import BaseTestCase, CommonTestCases
from unittest.mock import Mock, patch

from fixtures.events.end_event_fixtures import (
    end_event_mutation,
    end_event_mutation_response,
    end_unchecked_in_event_mutation,
    end_unchecked_in_event_mutation_response,
    end_event_twice_mutation_response,
    wrong_calendar_id_end_event_mutation,
)
from fixtures.events.event_checkin_fixtures import (
    event_checkin_mutation,
    event_checkin_response
)


class TestEndEvent(BaseTestCase):

    @patch('api.events.schema.notify_slack.delay')
    def test_end_event(self, mock_notify_slack):
        """
        Test user can end an event
        """
        mock_notify_slack.return_value = True
        CommonTestCases.user_token_assert_equal(
            self,
            event_checkin_mutation,
            event_checkin_response
        )
        CommonTestCases.user_token_assert_equal(
            self,
            end_event_mutation,
            end_event_mutation_response
        )

    def test_end_unchecked_in_event(self):
        """
        Test user cannot end an event before checking in
        """
        CommonTestCases.user_token_assert_in(
            self,
            end_unchecked_in_event_mutation,
            end_unchecked_in_event_mutation_response
        )

    @patch('api.events.schema.notify_slack.delay')
    def test_end_event_twice(self, mock_notify_slack):
        """
        Test user cannot end an event twice
        """
        mock_notify_slack.return_value = True
        CommonTestCases.user_token_assert_equal(
            self,
            event_checkin_mutation,
            event_checkin_response
        )
        CommonTestCases.user_token_assert_equal(
            self,
            end_event_mutation,
            end_event_mutation_response
        )
        CommonTestCases.user_token_assert_in(
            self,
            end_event_mutation,
            end_event_twice_mutation_response
        )

    def test_end_event_with_invalid_calendar_id(self):
        """
        Test user cannot end event with invalid calendar ID
        """
        CommonTestCases.user_token_assert_in(
            self,
            wrong_calendar_id_end_event_mutation,
            "This Calendar ID is invalid"
        )
