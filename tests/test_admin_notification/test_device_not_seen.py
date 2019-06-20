from tests.base import BaseTestCase, CommonTestCases
from fixtures.token.token_fixture import ADMIN_TOKEN
from fixtures.admin_notification.admin_notification_fixtures import (
    get_all_unread_notifications, get_all_unread_notifications_response,
    get_all_unread_notifications_notifications_off_response)
from fixtures.devices.devices_fixtures import devices_query
from admin_notifications.helpers.device_last_seen import (
    notify_when_device_is_offline)
from api.notification.models import Notification


class TestDeviceOffline(BaseTestCase):
    def test_get_all_notifications(self):
        notification = Notification(id=1, user_id=1, device_health_notification=True,
            meeting_update_notification=True, set_notifications_settings=True)
        notification.save()
        CommonTestCases.admin_token_assert_equal(
            self,
            get_all_unread_notifications,
            get_all_unread_notifications_response
        )

    def test_get_all_notifications_notifications_truned_off(self):
        notifications_turned_off = Notification(id=1, user_id=1, device_health_notification=True,
            meeting_update_notification=True, set_notifications_settings=False)
        notifications_turned_off.save()
        CommonTestCases.admin_token_assert_equal(
            self,
            get_all_unread_notifications,
            get_all_unread_notifications_notifications_off_response,
        )
    
    def test_when_device_is_offline(self):
        """
        Testing for device creation
        """
        headers = {"Authorization": "Bearer" + " " + ADMIN_TOKEN}
        self.app_test.post(devices_query, headers=headers)
        response = notify_when_device_is_offline()
        assert response[0].activity.value == 'offline'
