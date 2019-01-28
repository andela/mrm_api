from tests.base import BaseTestCase, CommonTestCases
from fixtures.devices.devices_fixtures import (
    update_device_query,
    query_with_non_existant_id,
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
            "DeviceId not found"
        )
