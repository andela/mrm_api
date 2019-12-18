from tests.base import BaseTestCase, CommonTestCases
from fixtures.devices.devices_fixtures import (
    devices_query,
    create_device_query_invalid_room
)
from fixtures.devices.devices_fixtures_responses import (
    devices_query_response
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

    def test_create_device_in_nonexistent_room_throws_errors(self):
        """
        Test for creation of device in invalid room id
        """
        CommonTestCases.lagos_admin_token_assert_in(
            self,
            create_device_query_invalid_room,
            "Room not found"
        )
