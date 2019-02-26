from unittest.mock import patch

from tests.base import BaseTestCase, CommonTestCases
from helpers.calendar.calendar import get_events_mock_data
from fixtures.room.most_booked_room_least_booked_rooms_fixtures import (
    get_bottom_ten_rooms,
    bottom_ten_response,
    get_top_ten_rooms,
    top_ten_response
)


@patch("helpers.calendar.analytics_helper.get_events_within_datetime_range",
       spec=True)
class QueryRoomsAnalytics(BaseTestCase):

    def test_bottom_ten_most_used_rooms(self, mock_get_json):
        mock_get_json.return_value = get_events_mock_data()
        CommonTestCases.admin_token_assert_equal(
            self,
            get_bottom_ten_rooms,
            bottom_ten_response
        )

    def test_top_ten_most_used_rooms(self, mock_get_json):
        mock_get_json.return_value = get_events_mock_data()
        CommonTestCases.admin_token_assert_equal(
            self,
            get_top_ten_rooms,
            top_ten_response
        )
