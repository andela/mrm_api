from tests.base import BaseTestCase, CommonTestCases
from fixtures.room_resource.get_rooms_with_resource_fixtures import (
    rooms_containing_resource_query,
    rooms_containing_resource_expected_response,
    rooms_containing_non_existent_resource_query,
    rooms_containing_non_existent_resource_expected_response
)
from fixtures.room.assign_resource_fixture import (
    assign_resource_mutation,
    assign_resource_mutation_response
    )


class TestGetRoomsWithResource(BaseTestCase):

    def test_query_rooms_containing_resource(self):
        """
        Test that an admin can get the rooms that have a particular resource
        by providing the resourceId
        """
        CommonTestCases.admin_token_assert_equal(
           self,
           assign_resource_mutation,
           assign_resource_mutation_response,
        )
        CommonTestCases.admin_token_assert_equal(
            self,
            rooms_containing_resource_query,
            rooms_containing_resource_expected_response
        )

    def test_query_rooms_containing_non_existent_resource(self):
        """
        Test that "Resource not found" error is returned if no resource with
        provided resourceId exists
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            rooms_containing_non_existent_resource_query,
            rooms_containing_non_existent_resource_expected_response
        )
