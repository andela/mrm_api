import sys
import os
from unittest.mock import patch

from tests.base import BaseTestCase, CommonTestCases
from helpers.calendar.calendar import get_events_mock_data
from fixtures.room.room_calendar_ids_cleanup import (
    room_calendar_ids_cleanup_query,
    room_calendar_ids_cleanup_response_when_all_ids_are_valid
)

sys.path.append(os.getcwd())


@patch("utilities.calendar_ids_cleanup.get_google_calendar_events",
       spec=True)
class RoomsTableCleanup(BaseTestCase):

    def test_room_calendar_ids_cleanup_when_all_ids_are_valid(self,
                                                              mock_get_json):
        mock_get_json.return_value = get_events_mock_data()
        CommonTestCases.admin_token_assert_equal(
            self,
            room_calendar_ids_cleanup_query,
            room_calendar_ids_cleanup_response_when_all_ids_are_valid
        )
