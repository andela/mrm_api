from unittest.mock import patch

from tests.base import BaseTestCase, CommonTestCases
from helpers.calendar.calendar import get_events_mock_data
from fixtures.room.room_analytics_duration_fixtures import (
    get_daily_meetings_total_duration_query,
    get_daily_meetings_total_duration_response,
    get_weekly_meetings_total_duration_query,
    get_weekly_meetings_total_duration_response,
    get_paginated_meetings_total_duration_query,
    get_paginated_meetings_total_duration_response,
    get_paginated_meetings_total_duration_query_invalid_page,
    get_paginated_meetings_total_duration_invalid_page_result,
    meetings_total_duration_query_for_a_future_date
)


@patch("helpers.calendar.analytics_helper.get_events_within_datetime_range",
       spec=True)
class TotalDailyDurations(BaseTestCase):

    def test_total_daily_durations(self, mock_get_json):
        """
        Tests getting total durations for daily meetings
        """
        mock_get_json.return_value = get_events_mock_data()
        CommonTestCases.admin_token_assert_equal(
            self,
            get_daily_meetings_total_duration_query,
            get_daily_meetings_total_duration_response
        )

    def test_total_weekly_durations(self, mock_get_json):
        """
        Tests getting total durations for weekly meetings
        """
        mock_get_json.return_value = get_events_mock_data()
        CommonTestCases.admin_token_assert_equal(
            self,
            get_weekly_meetings_total_duration_query,
            get_weekly_meetings_total_duration_response
        )

    def test_paginated_meetings_total_duration(self, mock_get_json):
        """
        Tests getting the paginated total durations for meetings
        """
        mock_get_json.return_value = get_events_mock_data()
        CommonTestCases.admin_token_assert_equal(
            self, get_paginated_meetings_total_duration_query,
            get_paginated_meetings_total_duration_response)

    def test_paginated_meetings_total_duration_invalid_page(self,
                                                            mock_get_json):
        """
        Tests getting the paginated total durations for meetings
        """
        mock_get_json.return_value = get_events_mock_data()
        CommonTestCases.admin_token_assert_equal(
            self, get_paginated_meetings_total_duration_query_invalid_page,
            get_paginated_meetings_total_duration_invalid_page_result)

    def test_analytics_meeting_durations_future_date(self, mock_get_json):
        """
        Test for querying data that does not apply in the future
        """
        mock_get_json.return_value = get_events_mock_data()
        CommonTestCases.admin_token_assert_in(
            self, meetings_total_duration_query_for_a_future_date,
            "Invalid date. You can not retrieve data beyond today"
        )
