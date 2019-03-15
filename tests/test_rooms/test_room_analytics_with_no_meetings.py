from unittest.mock import patch

from tests.base import BaseTestCase, CommonTestCases
from helpers.calendar.calendar import get_events_mock_data
from fixtures.room.most_booked_room_least_booked_rooms_fixtures import (
    test_for_no_meetings,
    test_for_no_meetings_response
)
from fixtures.room.room_analytics_least_used_fixtures import (
    get_room_usage_no_meetings_analytics,
    get_room_usage_no_meetings_anaytics_response
)
from fixtures.room.room_analytics_duration_fixtures import (
    get_weekly_meetings_total_duration_no_meetings_query,
    get_weekly_meetings_total_duration_no_meetings_response
)

events = get_events_mock_data()


class QueryRoomsEmptyAnalytics(BaseTestCase):

    @patch("helpers.calendar.analytics_helper.get_events_within_datetime_range",
           spec=True)
    def test_for_rooms_with_no_meetings(self, mock_get_json):
        mock_get_json.return_value = events
        events['items'].clear()
        CommonTestCases.admin_token_assert_equal(
            self,
            test_for_no_meetings,
            test_for_no_meetings_response
        )

    @patch("helpers.calendar.analytics_helper.get_events_within_datetime_range",
           spec=True)
    def test_for_room_usage_with_no_meetings(self, mock_get_json):
        mock_get_json.return_value = events
        events['items'].clear()
        CommonTestCases.admin_token_assert_equal(
            self,
            get_room_usage_no_meetings_analytics,
            get_room_usage_no_meetings_anaytics_response
        )

    @patch("helpers.calendar.analytics_helper.get_events_within_datetime_range",
           spec=True)
    def test_for_meeting_duration_with_no_meetings(self, mock_get_json):
        mock_get_json.return_value = events
        events['items'].clear()
        CommonTestCases.admin_token_assert_equal(
            self,
            get_weekly_meetings_total_duration_no_meetings_query,
            get_weekly_meetings_total_duration_no_meetings_response
        )
