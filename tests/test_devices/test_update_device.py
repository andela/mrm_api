from tests.base import BaseTestCase, CommonTestCases
from fixtures.devices.devices_fixtures import (
    update_device_query,
    query_with_non_existant_id,
    update_device_activity_mutation,
    expected_update_device_activity_response,
    query_non_existent_device_id
)


class TestUpdateDevices(BaseTestCase):
    def test_update_device(self):
        CommonTestCases.admin_token_assert_in(
            self,
            update_device_query,
            "Apple tablet"
        )

    def test_update_device_with_non_existant_id(self):
        CommonTestCases.admin_token_assert_in(
            self,
            query_with_non_existant_id,
            "Device ID not found"
        )

    def test_update_device_activity(self):

        CommonTestCases.admin_token_assert_equal(
            self,
            update_device_activity_mutation,
            expected_update_device_activity_response
        )

    def test_update_device_activity_with_non_existent_id(self):
        CommonTestCases.admin_token_assert_in(
            self,
            query_non_existent_device_id,
            "Device not found"
        )
