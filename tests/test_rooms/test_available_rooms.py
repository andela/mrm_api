from unittest.mock import patch
from tests.base import BaseTestCase, CommonTestCases
from helpers.calendar.calendar import get_calendar_list_mock_data

from fixtures.room.available_rooms_fixtures import (
    available_rooms_query,
    available_rooms_query_with_empty_input,
    available_rooms_query_when_startDate_is_bigger_than_endDate,
    available_rooms_query_when_startTime_is_bigger_than_endTime
)


class AvailableRooms(BaseTestCase):

    @patch("api.room.schema_query.get_google_api_calendar_list", spec=True,
           return_value=get_calendar_list_mock_data())
    def test_available_rooms(self, mock_get_json):
        CommonTestCases.admin_token_assert_in(
            self,
            available_rooms_query,
            "No available rooms at the moment"
        )

    def available_rooms_query_with_empty_input(self):
        CommonTestCases.admin_token_assert_in(
            self,
            available_rooms_query_with_empty_input,
            "startDate argument missing"
        )

    def available_rooms_query_when_startDate_is_bigger_than_endDate(self):
        CommonTestCases.admin_token_assert_in(
            self,
            available_rooms_query_when_startDate_is_bigger_than_endDate,
            "Start date must be lower than end date"
        )

    def available_rooms_query_when_startTime_is_bigger_than_endTime(self):
        CommonTestCases.admin_token_assert_in(
            self,
            available_rooms_query_when_startTime_is_bigger_than_endTime,
            "Start time must be lower than end time"
        )
