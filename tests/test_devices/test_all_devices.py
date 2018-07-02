from tests.base import BaseTestCase
from fixtures.devices.devices_fixtures import (
    query_devices,
    expected_response_devices
)

import sys
import os
sys.path.append(os.getcwd())


class TestAllDevices(BaseTestCase):
    def test_all_devices(self):
        query = self.client.execute(query_devices)
        self.assertEquals(query, expected_response_devices)
