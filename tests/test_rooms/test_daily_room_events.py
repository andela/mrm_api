from tests.base import BaseTestCase, CommonTestCases
from fixtures.room.daily_room_events_fixture import (
    daily_room_events_query, daily_room_events_response,
    daily_room_events_wrong_date_format_query,
    daily_events_wrong_date_format_response,
    paginated_daily_room_events_query,
    daily_paginated_room_events_response,
    invalid_page_for_analytics_for_daily_events_query
)


class TestDailyEvents(BaseTestCase):

    def test_analytics_for_daily_events(self):
        """
            Test querying analytics for daily events
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            daily_room_events_query,
            daily_room_events_response
        )

    def test_analytics_for_daily_events_wrong_format_date(self):
        """
            Test querying analytics for daily events with
            wrong date formats
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            daily_room_events_wrong_date_format_query,
            daily_events_wrong_date_format_response
        )

    def test_analytics_for_daily_events_pagination(self):
        """
            Test querying analytics for daily room events
            data with pagination
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            paginated_daily_room_events_query,
            daily_paginated_room_events_response
        )

    def test_fetching_invalid_page_for_paginated_analytics_for_daily_events(
        self
    ):
        """
            Test fetching a non-existing page in paginated analytics for
            daily room events
        """
        CommonTestCases.admin_token_assert_in(
            self,
            invalid_page_for_analytics_for_daily_events_query,
            'Page does not exist'
        )
