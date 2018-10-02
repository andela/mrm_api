from tests.base import BaseTestCase, CommonTestCases
from fixtures.room.room_analytics_duration_fixtures import (
    get_daily_meetings_total_duration_query,
    get_daily_meetings_total_duration_response,
    get_weekly_meetings_total_duration_query,
    get_weekly_meetings_total_duration_response
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

    def test_total_weekly_durations(self):
        """
        Tests getting total durations for weekly meetings
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            get_weekly_meetings_total_duration_query,
            get_weekly_meetings_total_duration_response
        )
