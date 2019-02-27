from tests.base import BaseTestCase, CommonTestCases
from helpers.database import engine, db_session
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

    def test_database_connection_error(self):
        """
        test a user friendly message is returned to a user when database
        cannot be reached
        """
        BaseTestCase().tearDown()
        CommonTestCases.admin_token_assert_in(
            self,
            update_device_query,
            "The database cannot be reached"
        )

    def test_update_device_without_devices_model(self):
        """
        test a user cannot update a device when the device model is missing
        """
        db_session.remove()
        with engine.begin() as conn:
            conn.execute("DROP TABLE devices CASCADE")
        CommonTestCases.admin_token_assert_in(
            self,
            update_device_query,
            "does not exist"
        )
