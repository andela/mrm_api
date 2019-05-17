from tests.base import BaseTestCase, CommonTestCases
from fixtures.devices.devices_fixtures import (
    query_device,
    expected_response_device,
    query_non_existent_device,
    expected_error_non_existent_device_id
)

import sys
import os
sys.path.append(os.getcwd())


class TestGetSpecificDevice(BaseTestCase):
    """
    Test that an admin can query to get
    a list of all devices in their location
    """
    def test_specific_device(self):
        CommonTestCases.admin_token_assert_equal(
            self,
            query_device,
            expected_response_device
        )

    def test_get_non_existing_device(self):
        CommonTestCases.admin_token_assert_equal(
            self,
            query_non_existent_device,
            expected_error_non_existent_device_id
        )
