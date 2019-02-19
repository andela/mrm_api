import sys
import os

from tests.base import BaseTestCase, CommonTestCases
from fixtures.room_resource.delete_room_resource import (  # noqa: F401
  delete_resource,
  expected_query_after_delete,
  delete_non_existant_resource,
  response_for_delete_room_resource_with_database_error
  )
from helpers.database import db_session, engine  # noqa: F401


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
            "Resource not found"
        )

    def test_non_existant_deleteresource_mutation(self):
        CommonTestCases.admin_token_assert_in(
            self,
            delete_non_existant_resource,
            "Resource not found"
        )

    def test_database_connection_error(self):
        """
        test a user friendly message is returned to a user when database
        cannot be reached
        """
        BaseTestCase().tearDown()
        CommonTestCases.admin_token_assert_in(
            self,
            delete_resource,
            "The database cannot be reached"
            )

    def test_delete_resource_without_resourse_model(self):
        db_session.remove()
        with engine.begin() as conn:
            conn.execute("DROP TABLE resources CASCADE")
        CommonTestCases.admin_token_assert_equal(
            self,
            delete_resource,
            response_for_delete_room_resource_with_database_error
        )
