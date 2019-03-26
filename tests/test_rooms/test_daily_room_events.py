from unittest.mock import patch

from tests.base import BaseTestCase, CommonTestCases
from helpers.calendar.calendar import get_events_mock_data
from fixtures.room.daily_room_events_fixture import (
    daily_room_events_query, daily_room_events_response,
    daily_room_events_wrong_date_format_query,
    daily_events_wrong_date_format_response,
    paginated_daily_room_events_query,
    daily_paginated_room_events_response,
    invalid_page_for_analytics_for_daily_events_query
)


@patch("helpers.calendar.analytics_helper.get_events_within_datetime_range",
       spec=True)
class TestDailyEvents(BaseTestCase):

    def test_analytics_for_daily_events(self, mock_get_json):
        """
            Test querying analytics for daily events returns
            correct data
        """
        mock_get_json.return_value = get_events_mock_data()
        CommonTestCases.admin_token_assert_equal(
            self,
            daily_room_events_query,
            daily_room_events_response
        )

    def test_analytics_for_daily_events_wrong_format_date(self, mock_get_json):
        """
            Test querying analytics for daily events with
            wrong date formats fails with correct error message
        """
        mock_get_json.return_value = get_events_mock_data()
        CommonTestCases.admin_token_assert_equal(
            self,
            daily_room_events_wrong_date_format_query,
            daily_events_wrong_date_format_response
        )

    def test_analytics_for_daily_events_pagination(self, mock_get_json):
        """
            Test querying analytics for daily room events
            data with pagination returns correct paginated data
        """
        mock_get_json.return_value = get_events_mock_data()
        CommonTestCases.admin_token_assert_equal(
            self,
            paginated_daily_room_events_query,
            daily_paginated_room_events_response
        )

    def test_fetching_invalid_page_for_paginated_analytics_for_daily_events(
        self, mock_get_json
    ):
        """
            Test fetching a non-existing page in paginated analytics for
            daily room events fails with correct error message
        """
        mock_get_json.return_value = get_events_mock_data()
        CommonTestCases.admin_token_assert_in(
            self,
            invalid_page_for_analytics_for_daily_events_query,
            'Page does not exist'
        )
