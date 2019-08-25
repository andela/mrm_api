from tests.base import BaseTestCase, CommonTestCases
from fixtures.devices.devices_fixtures import (
    delete_device_mutation,
    delete_non_exiting_device_mutation,
    delete_device_response)


class TestDeleteDevices(BaseTestCase):
    def test_delete_device(self):
        CommonTestCases.admin_token_assert_equal(
            self,
            delete_device_mutation,
            delete_device_response
        )

    def test_delete_non_existing_device(self):
        CommonTestCases.admin_token_assert_in_errors(
            self,
            delete_non_exiting_device_mutation,
            "Device not found"
        )
