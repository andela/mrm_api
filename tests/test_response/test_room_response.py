import sys
import os
from tests.base import BaseTestCase, CommonTestCases
from fixtures.response.room_response_fixture import (
   get_room_response_query,
   get_room_response_query_response,
   get_room_response_non_existence_room_id
)


sys.path.append(os.getcwd())


class TestRoomResponse(BaseTestCase):

    def test_room_response(self):
        """
        Testing for room response

        """
        CommonTestCases.admin_token_assert_equal(
            self,
            get_room_response_query,
            get_room_response_query_response
        )

    def test_room_response_non_existence_room_id(self):
        """
        Testing for room response with non-existent
        room id

        """
        CommonTestCases.admin_token_assert_in(
            self,
            get_room_response_non_existence_room_id,
            "Non-existent room id"
        )
