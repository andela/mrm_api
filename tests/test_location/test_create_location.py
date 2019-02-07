from tests.base import BaseTestCase, CommonTestCases
from fixtures.location.create_location_fixtures import (
    create_location_query,
    create_location_with_invalid_url,
    create_duplicate_location_query, create_location_with_invalid_timezone

)

import sys
import os
sys.path.append(os.getcwd())


class TestCreateLocation(BaseTestCase):

    def test_location_creation(self):
        """
        Testing for location creation
        """
        CommonTestCases.admin_token_assert_in(
            self,
            create_location_query,
            'Location created but email not sent')

    def test_location_creation_with_invalid_image_url(self):
        """
        Testing for location creation with invalid url
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

    def test_location_that_already_exists(self):
        """
        Testing for location that had been created
        """
        CommonTestCases.admin_token_assert_in(
            self,
            create_duplicate_location_query,
            'Kampala Location already exists')
