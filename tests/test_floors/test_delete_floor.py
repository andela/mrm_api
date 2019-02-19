from tests.base import BaseTestCase, CommonTestCases

from helpers.database import engine, db_session
from fixtures.floor.delete_floor_fixtures import (
    delete_floor_mutation,
    delete_with_nonexistent_floor_id,
    response_for_delete_floor_with_database_error
)


class TestDeleteRoom(BaseTestCase):
    def test_delete_floor_admin_user(self):
        CommonTestCases.admin_token_assert_in(
            self,
            delete_floor_mutation,
            "3rd"
        )

    def test_delete_floor_non_admin_user(self):
        CommonTestCases.user_token_assert_in(
            self,
            delete_floor_mutation,
            "You are not authorized to perform this action"
        )

    def test_non_existant_floor_id(self):
        CommonTestCases.admin_token_assert_in(
            self,
            delete_with_nonexistent_floor_id,
            "Floor not found"
        )

    def test_database_connection_error(self):
        """
        test a user friendly message is returned to a user when database
        cannot be reached
        """
        BaseTestCase().tearDown()
        CommonTestCases.admin_token_assert_in(
            self,
            delete_floor_mutation,
            "The database cannot be reached"
            )

    def test_delete_floors_without_floors_relation(self):
        """
        Testing for floor creation without floor relation
        """
        db_session.remove()
        with engine.begin() as conn:
            conn.execute("DROP TABLE floors CASCADE")
        CommonTestCases.admin_token_assert_equal(
          self,
          delete_floor_mutation,
          response_for_delete_floor_with_database_error
        )
