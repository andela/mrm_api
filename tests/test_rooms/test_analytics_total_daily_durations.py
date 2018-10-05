from tests.base import BaseTestCase, CommonTestCases
from fixtures.room.room_analytics_daily_duration_fixtures import (
    get_daily_meetings_total_duration_query,
    get_daily_meetings_total_duration_response
)


class TotalDailyDurations(BaseTestCase):

    def test_total_daily_durations(self):
        """
        Tests getting total durations for daily meetings
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            get_daily_meetings_total_duration_query,
            get_daily_meetings_total_duration_response
        )
