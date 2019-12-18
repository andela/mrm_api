from tests.base import BaseTestCase, CommonTestCases
from fixtures.response.room_response_fixture import (
    get_resolved_room_responses_query,
    get_resolved_room_responses_query_data
)
from fixtures.response.room_all_resolved_response_fixture import (
    all_resolved_room_response_query,
    all_resolved_room_response_data
)
from fixtures.response.room_mark_response_fixture import (
    mark_multiple_as_resolved_mutation,
    mark_multiple_as_unresolved_mutation,
    mark_multiple_as_resolved_with_invalid_id,
    mark_multiple_as_resolved_response,
    mark_multiple_as_unresolved_response
)
from fixtures.response.room_search_response_fixture import (
    search_resolved_responses_by_room_name,
    search_resolved_responses_by_room_name_data
)


class TestRoomResponse(BaseTestCase):
    def test_query_resolved_room_responses(self):
        """
        Test querying for resolved room responses
        """
        CommonTestCases.admin_token_assert_equal(
            self, get_resolved_room_responses_query,
            get_resolved_room_responses_query_data
        )

    def test_all_resolved_room_responses(self):
        """
        Test fetching all resolved responses in all rooms

        """
        CommonTestCases.admin_token_assert_equal(
            self,
            all_resolved_room_response_query,
            all_resolved_room_response_data
        )

    def test_search_resolved_responses_by_room_name(self):
        """
        Testing for searching all resolved room responses
        by room name
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            search_resolved_responses_by_room_name,
            search_resolved_responses_by_room_name_data
        )

    def test_mark_multiple_responses_as_resolved(self):
        """
            Tests that admin can mark multiple responses
            as resolved
        """
        CommonTestCases.admin_token_assert_equal(
            self, mark_multiple_as_resolved_mutation,
            mark_multiple_as_resolved_response)

    def test_mark_multiple_responses_as_unresolved(self):
        """
            Tests that admin can mark multiple responses
            as unresolved
        """
        CommonTestCases.admin_token_assert_equal(
            self, mark_multiple_as_unresolved_mutation,
            mark_multiple_as_unresolved_response)

    def test_mark_multiple_responses_as_resolved_with_invalid_id(self):
        """
            Tests that admin can not mark multiple responses
            as resolved with invalid response Id
        """
        CommonTestCases.admin_token_assert_in(
            self, mark_multiple_as_resolved_with_invalid_id,
            "Response 36 does not exist")
