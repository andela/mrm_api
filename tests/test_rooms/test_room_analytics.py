from tests.base import BaseTestCase, CommonTestCases
from fixtures.room.room_analytics_fixtures import (
    get_most_used_room_in_a_month_analytics_query,
    get_most_used_room_in_a_month_analytics_response,
    most_used_room_in_a_month_analytics_invalid_location_query,
    most_used_room_in_a_month_analytics_invalid_location_response,
    get_least_used_room_per_week_query,
    get_least_used_room_per_week_response,
    get_least_used_room_without_event_query,
    get_least_used_room_without_event_response,
    get_room_usage_analytics,
    get_room_usage_anaytics_respone,
    get_room_usage_analytics_invalid_location,
    get_room_usage_analytics_invalid_location_response,
    get_least_used_room_per_month,
    get_least_used_room_per_month_response,
    get_least_used_room_per_month_invalid_location,
    response_least_used_room_per_month_invalid_location,
    get_most_used_room_per_week_query,
    get_most_used_room_per_week_response,
    get_most_used_room_without_event_query,
    get_most_used_room_without_event_response

)
from fixtures.room.room_monthly_meeting_duration_fixtures import (
    get_monthly_meetings_total_duration_query,
    get_monthly_meetings_total_duration_response
)


class QueryRoomsAnalytics(BaseTestCase):

    def test_most_used_room_in_a_month_analytics(self):
        CommonTestCases.admin_token_assert_equal(
            self,
            get_most_used_room_in_a_month_analytics_query,
            get_most_used_room_in_a_month_analytics_response
        )

    def test_most_used_room_in_a_month_invalid_location_analytics(self):
        CommonTestCases.admin_token_assert_equal(
            self,
            most_used_room_in_a_month_analytics_invalid_location_query,
            most_used_room_in_a_month_analytics_invalid_location_response
        )

    def test_analytics_for_least_used_room_weekly(self):
        CommonTestCases.admin_token_assert_equal(
            self,
            get_least_used_room_per_week_query,
            get_least_used_room_per_week_response
        )

    def test_analytics_for_least_used_room_without_event_weekly(self):
        CommonTestCases.admin_token_assert_equal(
            self,
            get_least_used_room_without_event_query,
            get_least_used_room_without_event_response
        )

    def test_room_usage_analytics(self):
        CommonTestCases.admin_token_assert_equal(
            self,
            get_room_usage_analytics,
            get_room_usage_anaytics_respone
        )

    def test_room_usage_analytics_invalid_location(self):
        CommonTestCases.admin_token_assert_equal(
            self,
            get_room_usage_analytics_invalid_location,
            get_room_usage_analytics_invalid_location_response
        )

    def test_analytics_for_least_used_room_monthly(self):
        CommonTestCases.admin_token_assert_equal(
            self,
            get_least_used_room_per_month,
            get_least_used_room_per_month_response
        )

    def test_analytics_for_least_used_room_monthly_invalid_location(self):
        CommonTestCases.admin_token_assert_equal(
            self,
            get_least_used_room_per_month_invalid_location,
            response_least_used_room_per_month_invalid_location
        )

    def test_analytics_for_most_used_room_weekly(self):
        CommonTestCases.admin_token_assert_equal(
            self,
            get_most_used_room_per_week_query,
            get_most_used_room_per_week_response
        )

    def test_analytics_for_most_used_room_without_event_weekly(self):
        CommonTestCases.admin_token_assert_equal(
            self,
            get_most_used_room_without_event_query,
            get_most_used_room_without_event_response
        )

    def test_total_monthly_meeting_durations(self):
        CommonTestCases.admin_token_assert_equal(
            self,
            get_monthly_meetings_total_duration_query,
            get_monthly_meetings_total_duration_response
        )
