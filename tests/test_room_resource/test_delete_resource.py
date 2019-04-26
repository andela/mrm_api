import sys
import os

from tests.base import BaseTestCase, CommonTestCases
from fixtures.room_resource.delete_room_resource import (
  delete_resource, expected_response_after_delete, delete_non_existent_resource)


sys.path.append(os.getcwd())


class TestDeleteRoomResource(BaseTestCase):

    def test_delete_resource_mutation_when_not_admin(self):
        """
             Test user connot delete resource when not an admin
        """
        CommonTestCases.user_token_assert_in(
            self,
            delete_resource,
            "You are not authorized to perform this action"
        )

    def test_delete_resource_mutation_when_admin(self):
        """
            Test successful soft delete of a resource by an admin.
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            delete_resource,
            expected_response_after_delete
        )

    def test_delete_non_existent_resource(self):
        """
            Test that admin user cannot delete a resource that doesn't exist
            in the database.
        """
        CommonTestCases.admin_token_assert_in(
            self,
            delete_non_existent_resource,
            "Resource not found"
        )

    def test_delete_already_deleted_resource(self):
        """
            Test that admin user cannot delete a resource that has already been
            soft deleted.
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            delete_resource,
            expected_response_after_delete
        )
        CommonTestCases.admin_token_assert_in(
            self,
            delete_resource,
            "Resource not found"
        )
