import sys
import os
from tests.base import BaseTestCase, CommonTestCases
from fixtures.events.events_ratios_fixtures import (
    event_ratio_query,
    event_ratio_response
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
