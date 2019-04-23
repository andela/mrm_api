from tests.base import BaseTestCase, CommonTestCases
from fixtures.room_resource.update_assigned_resource import (
    update_assigned_resource_query,
    update_assigned_resource_query_response,
    update_with_negative_quantity,
    update_non_existing_room,
    update_non_existing_resource
)
from fixtures.room.assign_resource_fixture import (
    assign_resource_mutation,
    assign_resource_mutation_response
)


class TestUpdateAssignedResorce(BaseTestCase):

    def test_update_assigned_resource_by_non_admin(self):
        """
        Test that only an admin can update an
        assigned resource
        """
        CommonTestCases.user_token_assert_in(
            self,
            update_assigned_resource_query,
            "You are not authorized to perform this action"
        )

    def test_update_assigned_resource_by_admin(self):
        """
        Test that an admin can update an assigned resource
        """
        CommonTestCases.admin_token_assert_equal(
           self,
           assign_resource_mutation,
           assign_resource_mutation_response,
        )
        CommonTestCases.admin_token_assert_equal(
            self,
            update_assigned_resource_query,
            update_assigned_resource_query_response
        )

    def test_update_assigned_resource_with_negative_quantity(self):
        """
        Test that an admin cannot update a resource
        with a negative quantity
        """
        CommonTestCases.admin_token_assert_equal(
           self,
           assign_resource_mutation,
           assign_resource_mutation_response,
        )
        CommonTestCases.admin_token_assert_in(
            self,
            update_with_negative_quantity,
            "Assigned quantity cannot be less than zero"
        )

    def test_update_with_non_existing_room(self):
        """
        Test that an admin can not update a
        non existing room in the room_resources table
        """
        CommonTestCases.admin_token_assert_equal(
           self,
           assign_resource_mutation,
           assign_resource_mutation_response,
        )
        CommonTestCases.admin_token_assert_in(
            self,
            update_non_existing_room,
            "Room has no assigned resource"
        )

    def test_update_with_non_existing_resource(self):
        """
        Test that an admin can not update a
        non existing resource in the room_resources table
        """
        CommonTestCases.admin_token_assert_equal(
           self,
           assign_resource_mutation,
           assign_resource_mutation_response,
        )
        CommonTestCases.admin_token_assert_in(
            self,
            update_non_existing_resource,
            "Resource does not exist in the room"
        )
