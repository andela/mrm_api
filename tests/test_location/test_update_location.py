from tests.base import BaseTestCase, CommonTestCases

from helpers.database import engine, db_session
from fixtures.location.update_location_fixtures import (
    query_update_all_fields, query_location_id_non_existant,
    expected_query_update_all_fields, expected_location_id_non_existant_query,
    query_update_location_invalid_timezone,
    query_update_location_invalid_image_url)


class TestUpdateLocation(BaseTestCase):

    def test_if_all_fields_updated(self):
        CommonTestCases.admin_token_assert_equal(
            self, query_update_all_fields, expected_query_update_all_fields)

    def test_update_location_with_invalid_location_id(self):
        CommonTestCases.admin_token_assert_equal(
            self,
            query_location_id_non_existant,
            expected_location_id_non_existant_query
        )

    def test_update_location_with_invalid_timezone_throws_error(self):
        CommonTestCases.admin_token_assert_in(
            self,
            query_update_location_invalid_timezone,
            "Not a valid time zone"
        )

    def test_update_location_with_invalid_image_url_throws_error(self):
        CommonTestCases.admin_token_assert_in(
            self,
            query_update_location_invalid_image_url,
            "Please enter a valid image url")

    def test_database_connection_error(self):
        """
        test a user friendly message is returned to a user when database
        cannot be reached
        """
        BaseTestCase().tearDown()
        CommonTestCases.admin_token_assert_in(
            self,
            query_update_all_fields,
            "The database cannot be reached"
            )

    def test_update_location_without_location_relation(self):
        """
        Test a user cannot update a location without location relation
        """
        db_session.remove()
        with engine.begin() as conn:
            conn.execute("DROP TABLE locations CASCADE")
        CommonTestCases.admin_token_assert_in(
          self,
          query_update_all_fields,
          "does not exist"
        )
