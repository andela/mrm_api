from unittest.mock import patch

from tests.base import BaseTestCase, CommonTestCases
from helpers.calendar.calendar import get_events_mock_data
from fixtures.room.room_analytics_least_used_fixtures import (
    get_least_used_room_per_week_query,
    get_least_used_room_per_week_response,
    get_least_used_room_without_event_query,
    get_least_used_room_without_event_response,
    get_room_usage_analytics,
    get_room_usage_anaytics_response,
    get_least_used_room_per_month,
    get_least_used_room_per_month_response,
    analytics_for_least_used_room_day,
    analytics_for_least_used_room_day_response
)

from fixtures.room.room_analytics_most_used_fixtures import (
    get_most_used_room_in_a_month_analytics_query,
    get_most_used_room_in_a_month_analytics_response,
    get_most_used_room_per_week_query,
    get_most_used_room_per_week_response,
    get_most_used_room_without_event_query,
    get_most_used_room_without_event_response
)

from fixtures.room.room_monthly_meeting_duration_fixtures import (
    get_monthly_meetings_total_duration_query,
    get_monthly_meetings_total_duration_response
)

from fixtures.room.room_analytics_bookings_count_fixtures import (
    get_bookings_count_daily,
    get_bookings_count_daily_response,
    get_bookings_count_monthly,
    get_bookings_count_monthly_response,
    get_bookings_count_monthly_diff_years,
    get_bookings_count_monthly_diff_years_response,
)


@patch("helpers.calendar.analytics_helper.get_events_within_datetime_range",
       spec=True)
class QueryRoomsAnalytics(BaseTestCase):

    def test_most_used_room_in_a_month_analytics(self, mock_get_json):
        mock_get_json.return_value = get_events_mock_data()
        CommonTestCases.admin_token_assert_equal(
            self,
            get_most_used_room_in_a_month_analytics_query,
            get_most_used_room_in_a_month_analytics_response
        )

    def test_analytics_for_least_used_room_weekly(self, mock_get_json):
        mock_get_json.return_value = get_events_mock_data()
        CommonTestCases.admin_token_assert_equal(
            self,
            get_least_used_room_per_week_query,
            get_least_used_room_per_week_response
        )

    def test_analytics_for_least_used_room_without_event_weekly(self,
                                                                mock_get_json):
        mock_get_json.return_value = get_events_mock_data()
        CommonTestCases.admin_token_assert_equal(
            self,
            get_least_used_room_without_event_query,
            get_least_used_room_without_event_response
        )

    def test_room_usage_analytics(self, mock_get_json):
        mock_get_json.return_value = get_events_mock_data()
        CommonTestCases.admin_token_assert_equal(
            self,
            get_room_usage_analytics,
            get_room_usage_anaytics_response
        )

    def test_analytics_for_least_used_room_monthly(self, mock_get_json):
        mock_get_json.return_value = get_events_mock_data()
        CommonTestCases.admin_token_assert_equal(
            self,
            get_least_used_room_per_month,
            get_least_used_room_per_month_response
        )

    def test_analytics_for_most_used_room_weekly(self, mock_get_json):
        mock_get_json.return_value = get_events_mock_data()
        CommonTestCases.admin_token_assert_equal(
            self,
            get_most_used_room_per_week_query,
            get_most_used_room_per_week_response
        )

    def test_analytics_for_most_used_room_without_event_weekly(self,
                                                               mock_get_json):
        mock_get_json.return_value = get_events_mock_data()
        CommonTestCases.admin_token_assert_equal(
            self,
            get_most_used_room_without_event_query,
            get_most_used_room_without_event_response
        )

    def test_total_monthly_meeting_durations(self, mock_get_json):
        mock_get_json.return_value = get_events_mock_data()
        CommonTestCases.admin_token_assert_equal(
            self,
            get_monthly_meetings_total_duration_query,
            get_monthly_meetings_total_duration_response
        )

    def test_analytics_for_least_used_room_day(self, mock_get_json):
        mock_get_json.return_value = get_events_mock_data()
        CommonTestCases.admin_token_assert_equal(
            self,
            analytics_for_least_used_room_day,
            analytics_for_least_used_room_day_response
        )

    def test_analytics_for_daily_bookings(self, mock_get_json):
        mock_get_json.return_value = get_events_mock_data()
        CommonTestCases.admin_token_assert_equal(
            self, get_bookings_count_daily,
            get_bookings_count_daily_response
        )

    def test_analytics_for_monthly_bookings(self, mock_get_json):
        mock_get_json.return_value = get_events_mock_data()
        CommonTestCases.admin_token_assert_equal(
            self, get_bookings_count_monthly,
            get_bookings_count_monthly_response
        )

    def test_analytics_for_monthly_bookings_diff_years(self, mock_get_json):
        mock_get_json.return_value = get_events_mock_data()
        CommonTestCases.admin_token_assert_equal(
            self, get_bookings_count_monthly_diff_years,
            get_bookings_count_monthly_diff_years_response)
