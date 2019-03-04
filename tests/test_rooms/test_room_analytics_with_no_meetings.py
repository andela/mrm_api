from unittest.mock import patch

from tests.base import BaseTestCase, CommonTestCases
from helpers.calendar.calendar import get_events_mock_data
from fixtures.room.most_booked_room_least_booked_rooms_fixtures import (
    test_for_division_error
)

events = get_events_mock_data()


class QueryRoomsEmptyAnalytics(BaseTestCase):

    @patch("helpers.calendar.analytics_helper.get_events_within_datetime_range",
           spec=True)
    def test_for_percentage_division_error(self, mock_get_json):
        mock_get_json.return_value = events
        events['items'].clear()
        CommonTestCases.admin_token_assert_in(
            self,
            test_for_division_error,
            "There are no meetings"
        )
