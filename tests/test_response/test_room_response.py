import sys
import os
from tests.base import BaseTestCase, CommonTestCases
from fixtures.response.room_response_fixture import (
   get_room_response_query,
   get_room_response_query_response,
   get_room_response_non_existence_room_id,
   summary_room_response_query,
   summary_room_response_data,
   filter_by_response_query,
   filter_by_response_data,
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

    def test_summary_room_responses(self):
        """
        Testing for all responses in all rooms

        """
        CommonTestCases.admin_token_assert_equal(
            self,
            summary_room_response_query,
            summary_room_response_data
        )

    def test_filter_by_number_of_responses(self):
        """
        Testing for filtering the room responses
        by the number of responses the room has
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            filter_by_response_query,
            filter_by_response_data
        )
