from tests.base import BaseTestCase, CommonTestCases
from helpers.database import engine, db_session
from fixtures.location.delete_location_fixtures import (
    delete_location_query,
    delete_location_response,
    delete_non_existent_location,
    response_for_delete_location_with_database_error
)


class TestDeleteLocation(BaseTestCase):
    def test_delete_location(self):
        CommonTestCases.admin_token_assert_equal(
            self,
            delete_location_query,
            delete_location_response
        )

    def test_delete_non_existent_location(self):
        CommonTestCases.admin_token_assert_in(
            self,
            delete_non_existent_location,
            "location not found"
        )

    def test_database_connection_error(self):
        """
        test a user friendly message is returned to a user when database
        cannot be reached
        """
        BaseTestCase().tearDown()
        CommonTestCases.admin_token_assert_in(
            self,
            delete_location_query,
            "The database cannot be reached"
            )

    def test_delete_location_without_location_relation(self):
        """
        Testing for floor creation without floor relation
        """
        db_session.remove()
        with engine.begin() as conn:
            conn.execute("DROP TABLE locations CASCADE")
        CommonTestCases.admin_token_assert_equal(
          self,
          delete_location_query,
          response_for_delete_location_with_database_error
        )
