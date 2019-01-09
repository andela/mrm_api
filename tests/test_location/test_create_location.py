from tests.base import BaseTestCase, CommonTestCases
from fixtures.location.create_location_fixtures import (
    create_location_query,
    create_location_response)

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
