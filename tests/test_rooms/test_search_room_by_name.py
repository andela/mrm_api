import sys
import os


from tests.base import BaseTestCase, CommonTestCases
from fixtures.room.query_room_fixtures import (
    room_search_by_name,
    room_search_by_name_response,
    room_search_by_empty_name,
    room_search_by_empty_name_response,
    room_search_by_invalid_name,
    room_search_by_invalid_name_response
)

sys.path.append(os.getcwd())


class SearchRoomsByName(BaseTestCase):
    def test_search_room_by_name(self):
        CommonTestCases.user_token_assert_equal(
            self,
            room_search_by_name,
            room_search_by_name_response
        )

    def test_search_room_by_empty_name(self):
        CommonTestCases.user_token_assert_in(
            self,
            room_search_by_empty_name,
            room_search_by_empty_name_response
        )

    def test_search_room_by_invalid_name(self):
        CommonTestCases.user_token_assert_in(
            self,
            room_search_by_invalid_name,
            room_search_by_invalid_name_response
        )
