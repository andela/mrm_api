from tests.base import BaseTestCase
from fixtures.devices.devices_fixtures import (
    create_devices_query,
    expected_create_devices_response
)

import sys
import os
sys.path.append(os.getcwd())


class TestCreateRoom(BaseTestCase):

    def test_room_creation(self):
        """
        Testing for device creation
        """
        query = self.client.execute(create_devices_query)
        self.assertEqual(query, expected_create_devices_response)
