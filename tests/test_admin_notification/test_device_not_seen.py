from tests.base import BaseTestCase
from fixtures.token.token_fixture import ADMIN_TOKEN
from fixtures.devices.devices_fixtures import devices_query
from admin_notifications.helpers.device_last_seen import (
    notify_when_device_is_offline)


class TestDeviceOffline(BaseTestCase):
    def test_when_device_is_offline(self):
        """
        Testing for device creation
        """
        headers = {"Authorization": "Bearer" + " " + ADMIN_TOKEN}
        self.app_test.post(devices_query, headers=headers)
        response = notify_when_device_is_offline()
        assert response[0].activity.value == 'offline'
