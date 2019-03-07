from unittest.mock import patch

from tests.base import BaseTestCase, CommonTestCases
from helpers.calendar.calendar import get_events_mock_data
from fixtures.room.daily_room_events_fixture import (
    daily_room_events_query, daily_room_events_response,
    daily_room_events_wrong_date_format_query,
    daily_events_wrong_date_format_response,
)


@patch("helpers.calendar.analytics_helper.get_google_calendar_events",
       spec=True)
class TestDailyEvents(BaseTestCase):

    def test_analytics_for_daily_events(self, mock_get_json):
        mock_get_json.return_value = get_events_mock_data()
        CommonTestCases.admin_token_assert_equal(
            self,
            daily_room_events_query,
            daily_room_events_response
        )

    def test_analytics_for_daily_events_wrong_format_date(self, mock_get_json):
        mock_get_json.return_value = get_events_mock_data()
        CommonTestCases.admin_token_assert_equal(
            self,
            daily_room_events_wrong_date_format_query,
            daily_events_wrong_date_format_response
        )
