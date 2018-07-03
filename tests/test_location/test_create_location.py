from tests.base import BaseTestCase
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
        query = self.client.execute(create_location_query)
        expected_response = create_location_response
        self.assertEqual(query, expected_response)
