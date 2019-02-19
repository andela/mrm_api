from tests.base import BaseTestCase, CommonTestCases
from fixtures.location.create_location_fixtures import (
    create_location_query,
    create_location_response,
    create_location_query_wrong_country,
    create_location_query_wrong_time_zone,)

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

    def test_location_already_exists(self):
        """
        Testing location already exists
        """
        CommonTestCases.admin_token_assert_equal(
            self, create_location_query, create_location_response)
        CommonTestCases.admin_token_assert_in(
            self, create_location_query, 'New Location already exists')

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
        Testing for location creation
        """
        CommonTestCases.admin_token_assert_in(
            self,
            create_location_query_wrong_country,
            "Not a valid country"
        )

    def test_location_creation_with_invalid_time_zone(self):
        """
        Testing for location creation
        """
        CommonTestCases.admin_token_assert_in(
            self,
            create_location_query_wrong_time_zone,
            "Not a valid time zone"
        )
