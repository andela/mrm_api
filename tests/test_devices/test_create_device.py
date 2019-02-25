from tests.base import BaseTestCase, CommonTestCases
from fixtures.devices.devices_fixtures import (
    devices_query,
    devices_query_response,
    create_device_non_existant_room_id
)

from fixtures.token.token_fixture import ADMIN_TOKEN

import sys
import os
sys.path.append(os.getcwd())


class TestCreateDevice(BaseTestCase):

    def test_device_creation(self):
        """
        Testing for device creation
        """
        headers = {"Authorization": "Bearer" + " " + ADMIN_TOKEN}
        query = self.app_test.post(devices_query, headers=headers)
        self.assertEqual(query.data, devices_query_response)

    def test_device_creation_non_existant_room(self):
        """
        Testing for device creation where room doesn't exist
        """
        CommonTestCases.admin_token_assert_in(
            self,
            create_device_non_existant_room_id,
            "Room not found"
        )
