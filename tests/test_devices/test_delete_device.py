from tests.base import BaseTestCase, CommonTestCases
from fixtures.devices.devices_fixtures import (
    delete_device_mutation
)
from fixtures.devices.devices_fixtures_responses import (
    delete_device_response
)


class TestDeleteDevices(BaseTestCase):
    def test_delete_device(self):
        CommonTestCases.admin_token_assert_equal(
            self,
            delete_device_mutation,
            delete_device_response
        )
