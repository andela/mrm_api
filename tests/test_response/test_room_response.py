import sys
import os
from tests.base import BaseTestCase, CommonTestCases
from fixtures.response.room_response_fixture import (
    get_room_response_query,
    get_room_response_query_data,
    get_room_response_non_existence_room_id,
    search_response_by_room_invalid_room_query,
    search_response_by_room_query,
    search_response_by_room_only,
    search_response_by_room_beyond_limits_query,
    search_response_by_invalid_room,
    summary_room_response_query,
    summary_room_response_data,
    filter_by_response_query,
    filter_by_response_invalid_query,
    filter_by_response_data,
    query_paginated_responses,
    query_paginated_responses_response,
    query_paginated_responses_empty_page,
    mark_response_as_resolved_mutation,
    mark_user_response_as_resolved_mutation_response,
    mark_response_as_resolved_mutation_with_an_invalid_response_id,
    mark_a_user_response_as_unresolved_mutation,
    mark_a_user_response_as_unresolved_mutation_response,
    get_room_response_query_by_date,
    get_room_response_query_by_date_query,
    get_room_response_query_with_invalid_date,
    get_room_response_query_with_higher_lower_limit
)

sys.path.append(os.getcwd())


class TestRoomResponse(BaseTestCase):
    def test_room_response(self):
        """
        Testing for room response
        """
        CommonTestCases.admin_token_assert_equal(self, get_room_response_query,
                                                 get_room_response_query_data)

    def test_room_response_non_existence_room_id(self):
        """
        Testing for room response with non-existent
        room id
        """
        CommonTestCases.admin_token_assert_in(
            self, get_room_response_non_existence_room_id,
            "Non-existent room id")

    def test_summary_room_responses(self):
        """
        Testing for all responses in all rooms

        """
        CommonTestCases.admin_token_assert_equal(
            self, summary_room_response_query, summary_room_response_data)

    def test_filter_by_number_of_responses(self):
        """
        Testing for filtering the room responses
        by the number of responses the room has
        """
        CommonTestCases.admin_token_assert_equal(
            self, filter_by_response_query, filter_by_response_data)

    def test_filter_by_number_of_invalid_responses(self):
        """
        Testing for filtering the room responses
        by the number of responses the room has
        using ignoring one of the limits
        """
        CommonTestCases.admin_token_assert_in(
            self,
            filter_by_response_invalid_query,
            "Provide upper and lower limits to filter"
        )

    def test_filter_search_response_room_name(self):
        """
        Testing for filtering the room responses
        by the number and search by room name
        """
        CommonTestCases.admin_token_assert_equal(
            self, search_response_by_room_query, filter_by_response_data)

    def test_search_response_room_name_only(self):
        """
        Testing for searching the room responses
        by room name
        """
        CommonTestCases.admin_token_assert_equal(
            self, search_response_by_room_only, filter_by_response_data)

    def test_filter_search_response_invalid_room(self):
        """
        Test for filter by response and search
        the room with invalid room name
        """
        CommonTestCases.admin_token_assert_in(
            self, search_response_by_room_invalid_room_query,
            "No response for this room, enter a valid room name")

    def test_search_response_invalid_room(self):
        """
        Test for search by room name
        with invalid room name
        """
        CommonTestCases.admin_token_assert_in(
            self, search_response_by_invalid_room,
            "No response for this room, enter a valid room name")

    def test_search_response_beyond_limits(self):
        """
        Test for search by room name
        beyond upper and lower limits
        """
        CommonTestCases.admin_token_assert_in(
            self, search_response_by_room_beyond_limits_query,
            "No response for this room at this range")

    def test_get_paginated_responses(self):
        """
        Test for paginated responses
        """
        CommonTestCases.admin_token_assert_equal(
            self, query_paginated_responses,
            query_paginated_responses_response)

    def test_get_paginated_responses_empty_page(self):
        """
        Test for paginated responses for empty page
        """
        CommonTestCases.admin_token_assert_in(
            self, query_paginated_responses_empty_page, "Page does not exist")

    def test_mark_response_as_resolved_with_an_invalid_id(self):
        """
            Tests an admin can not mark
            a response that does not exist
            in the db as resolve
        """
        CommonTestCases.admin_token_assert_in(
            self,
            mark_response_as_resolved_mutation_with_an_invalid_response_id,
            "Response does not exist")

    def test_mark_response_as_resolved(self):
        """
            Tests an admin can mark a response
            as resolved
        """
        CommonTestCases.admin_token_assert_equal(
            self, mark_response_as_resolved_mutation,
            mark_user_response_as_resolved_mutation_response)

    def test_mark_response_as_unresolved(self):
        """
            Tests an admin can mark a response
            as unresolved
        """
        CommonTestCases.admin_token_assert_equal(
            self, mark_a_user_response_as_unresolved_mutation,
            mark_a_user_response_as_unresolved_mutation_response)

    def test_room_response_with_date_range(self):
        """
        Testing for room response with date range
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            get_room_response_query_by_date,
            get_room_response_query_by_date_query
        )

    def test_room_response_with_invalid_date(self):
        """
        Testing for room response with invalid/ future dates
        """
        CommonTestCases.admin_token_assert_in(
                self,
                get_room_response_query_with_invalid_date,
                "Dates should be before today"
            )

    def test_room_with_invalid_date_difference(self):
        """
        Testing for room response with higher lower limit
        """
        CommonTestCases.admin_token_assert_in(
                self,
                get_room_response_query_with_higher_lower_limit,
                "Earlier date should be lower than later date"
            )

    def test_database_connection_error(self):
        """
        test a user friendly message is returned to a user when database
        cannot be reached
        """
        BaseTestCase().tearDown()
        CommonTestCases.admin_token_assert_in(
            self,
            get_room_response_query,
            "The database cannot be reached"
            )
        CommonTestCases.admin_token_assert_in(
            self,
            summary_room_response_query,
            "The database cannot be reached"
            )
        CommonTestCases.admin_token_assert_in(
            self,
            filter_by_response_query,
            "The database cannot be reached"
            )
        CommonTestCases.admin_token_assert_in(
            self,
            search_response_by_room_only,
            "The database cannot be reached"
        )
