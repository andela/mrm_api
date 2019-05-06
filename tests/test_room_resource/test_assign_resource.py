import sys
import os

from tests.base import BaseTestCase, CommonTestCases
from fixtures.token.token_fixture import ADMIN_TOKEN
from fixtures.room.assign_resource_fixture import (
    assign_resource_mutation,
    assign_resource_mutation_response,
    assign_resource_non_existent_room,
    assign_non_existent_resource_id,
    assign_quantity_less_than_one,
    query_string
    )

sys.path.append(os.getcwd())


class TestAssignResource(BaseTestCase):

    def test_assign_resource(self):
        """
            Test that an admin can assign a resource to a room
        """
        CommonTestCases.admin_token_assert_equal(
           self,
           assign_resource_mutation,
           assign_resource_mutation_response,
        )

    def test_assign_non_existent_resource(self):
        """
            Test that admin cannot assign a
            resource which does not exist
        """
        CommonTestCases.admin_token_assert_in(
            self,
            assign_non_existent_resource_id,
            'Resource with such id does not exist.'
        )

    def test_assign_non_existent_room(self):
        """
            Test that an admin cannot assign a resource
            to a room that does not exist
        """
        CommonTestCases.admin_token_assert_in(
            self,
            assign_resource_non_existent_room,
            'Room not found'
        )

    def test_assign_quantity_less_than_one(self):
        """
           Test that an admin cannot assign a resource
           whose quantity is less than one
        """
        CommonTestCases.admin_token_assert_in(
            self,
            assign_quantity_less_than_one,
            'Assigned quantity cannot be less than 1.'
        )

    def test_assign_resource_multiple_times(self):
        """
            Test that an admin cannot assign a resource more than once
        """
        headers = {"Authorization": "Bearer" + " " + ADMIN_TOKEN}

        self.app_test.post(query_string, headers=headers)
        query2 = self.app_test.post(query_string, headers=headers)
        expected_response = "Resource already exists in the room."
        self.assertIn(expected_response, str(query2.data))
