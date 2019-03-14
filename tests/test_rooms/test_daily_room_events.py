from tests.base import BaseTestCase, CommonTestCases
from fixtures.room.daily_room_events_fixture import (
    daily_room_events_query, daily_room_events_response,
    daily_room_events_wrong_date_format_query,
    daily_events_wrong_date_format_response,
)


class TestDailyEvents(BaseTestCase):

    def test_analytics_for_daily_events(self):
        CommonTestCases.admin_token_assert_equal(
            self,
            daily_room_events_query,
            daily_room_events_response
        )

    def test_analytics_for_daily_events_wrong_format_date(self):
        CommonTestCases.admin_token_assert_equal(
            self,
            daily_room_events_wrong_date_format_query,
            daily_events_wrong_date_format_response
        )
