from tests.base import BaseTestCase, CommonTestCases
from fixtures.devices.devices_fixtures import (
    query_device,
    expected_response_device,
    query_non_existent_device,
    expected_error_non_existent_device_id
)
from fixtures.devices.devices_fixtures import (
    search_device_by_name,
    search_non_existing_device,
    search_device_by_name_expected_response,
    search_non_existing_device_response
)


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

    def test_search_device_by_name(self):
        CommonTestCases.admin_token_assert_equal(
            self,
            search_device_by_name,
            search_device_by_name_expected_response
        )

    def test_search_non_existing_device(self):
        CommonTestCases.admin_token_assert_equal(
            self,
            search_non_existing_device,
            search_non_existing_device_response
        )
