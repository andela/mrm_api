import sys
import os
from tests.base import BaseTestCase, CommonTestCases
from fixtures.events.get_recurring_events_fixtures import (
    recurring_event_query,
    # recurring_event_responce,
    # non_recurring_event_query,
    date_out_of_range_query,
    wrong_date_format_query
    # non_recurring_event_responce
)

sys.path.append(os.getcwd())


class TestRecurringEvent(BaseTestCase):

    def test_get_recurring_events(self):
        """
        test if the query returns all recurring events for a day
        """
        CommonTestCases.user_token_assert_in(
            self,
            recurring_event_query,
            "feb 28 2019"
        )

    def test_for_out_of_range_date_entry(self):
        '''
        test for incorrectly entered dates
        '''
        CommonTestCases.user_token_assert_in(
            self,
            date_out_of_range_query,
            "day is out of range for month"
        )

    def test_wrong_time_format(self):
        """
        test for dates entered in an incorrect format
        """
        CommonTestCases.user_token_assert_in(
            self,
            wrong_date_format_query,
            "does not match format"
        )
