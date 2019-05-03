from tests.base import BaseTestCase, CommonTestCases
from fixtures.devices.devices_fixtures import (
    query_devices,
    expected_response_devices
)

import sys
import os
sys.path.append(os.getcwd())


class TestAllDevices(BaseTestCase):
    """
    Test that an admin can query to get
    a list of all devices in their location
    """
    def test_all_devices(self):
        CommonTestCases.admin_token_assert_equal(
            self,
            query_devices,
            expected_response_devices
        )
