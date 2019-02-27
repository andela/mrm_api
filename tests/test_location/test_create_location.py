from tests.base import BaseTestCase, CommonTestCases
from helpers.database import engine, db_session
from fixtures.location.create_location_fixtures import (
    create_location_query,
    create_location_response,
    create_location_with_invalid_url,
    create_duplicate_location_query,
    create_location_with_invalid_timezone,
    create_location_query_wrong_country,
    create_location_query_wrong_time_zone)

import sys
import os
sys.path.append(os.getcwd())


class TestCreateLocation(BaseTestCase):

    def test_location_creation(self):
        """
        Testing for location creation
        """
        CommonTestCases.admin_token_assert_equal(
            self, create_location_query, create_location_response)

    def test_location_creation_with_invalid_image_url(self):
        """
        Testing for location creation with invalid image url
        """
        CommonTestCases.admin_token_assert_in(
            self,
            create_location_with_invalid_url,
            'Please enter a valid image url')

    def test_location_creation_with_invalid_timezone_field(self):
        """
        Testing for location creation with invalid timezone
        """
        CommonTestCases.admin_token_assert_in(
            self,
            create_location_with_invalid_timezone,
            'Not a valid time zone')

    def test_create_location_that_already_exists(self):
        """
        Testing for creating location that had already been created
        """
        CommonTestCases.admin_token_assert_in(
            self,
            create_duplicate_location_query,
            'Kampala Location already exists')

    def test_database_connection_error(self):
        """
        test a user friendly message is returned to a user when database
        cannot be reached
        """
        BaseTestCase().tearDown()
        CommonTestCases.admin_token_assert_in(
            self,
            create_location_query,
            "The database cannot be reached"
            )

    def test_location_creation_with_invalid_country(self):
        """
        Test a location cannot be created with invalid country
        """
        CommonTestCases.admin_token_assert_in(
            self,
            create_location_query_wrong_country,
            "Not a valid country"
        )

    def test_location_creation_with_invalid_time_zone(self):
        """
        Test a location cannot be created with invalid zone
        """
        CommonTestCases.admin_token_assert_in(
            self,
            create_location_query_wrong_time_zone,
            "Not a valid time zone"
        )

    def test_create_location_without_locations_model(self):
        """
        Test a user cannot create a location without location relation
        """
        db_session.remove()
        with engine.begin() as conn:
            conn.execute("DROP TABLE locations CASCADE")
        CommonTestCases.admin_token_assert_in(
            self,
            create_location_query,
            "does not exist"
        )
