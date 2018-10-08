import sys
import os

from tests.base import BaseTestCase, CommonTestCases
from fixtures.room_resource.delete_room_resource import (  # noqa: F401
  delete_resource, expected_query_after_delete, delete_non_existant_resource)  # noqa: E501
from helpers.database import db_session  # noqa: F401


sys.path.append(os.getcwd())


class TestDeleteRoomResource(BaseTestCase):

    def test_deleteresource_mutation_when_not_admin(self):
        CommonTestCases.user_token_assert_in(
            self,
            delete_resource,
            "You are not authorized to perform this action"
        )

    def test_deleteresource_mutation_when_admin(self):
        CommonTestCases.admin_token_assert_in(
            self,
            delete_resource,
            "Markers"
        )

    def test_non_existant_deleteresource_mutation(self):
        CommonTestCases.admin_token_assert_in(
            self,
            delete_non_existant_resource,
            "Resource not found"
        )
