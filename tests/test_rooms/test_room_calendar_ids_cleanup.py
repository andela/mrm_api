import sys
import os

from tests.base import BaseTestCase, CommonTestCases
from fixtures.room.room_calendar_ids_cleanup import (
    room_calendar_ids_cleanup_query,
    room_calendar_ids_cleanup_response_when_all_ids_are_valid
)

sys.path.append(os.getcwd())


class RoomsTableCleanup(BaseTestCase):

    def test_room_calendar_ids_cleanup_when_all_ids_are_valid(self):
        CommonTestCases.admin_token_assert_equal(
            self,
            room_calendar_ids_cleanup_query,
            room_calendar_ids_cleanup_response_when_all_ids_are_valid
        )
