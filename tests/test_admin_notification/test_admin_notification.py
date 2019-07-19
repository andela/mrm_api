from tests.base import BaseTestCase, CommonTestCases
from fixtures.admin_notification.admin_notification_fixtures import (
  get_all_unread_notifications,
  get_all_unread_notifications_response,
  get_all_unread_notifications_response_on_false, 
  change_notification_status_unexistent_id,
  change_notification_status_unexistent_id_response
)
from api.notification.models import Notification


class TestDeleteTag(BaseTestCase):
    def test_get_all_notifications(self):
        notification = Notification(id=1, user_id=1, device_health_notification=True,
          meeting_update_notification=True, get_notifications=True)
        notification.save()
        CommonTestCases.admin_token_assert_equal(
          self,
          get_all_unread_notifications,
          get_all_unread_notifications_response
        )

    def test_get_all_notifications_settings_off(self):
        notification = Notification(id=1, user_id=1, device_health_notification=True,
          meeting_update_notification=True, get_notifications=False)
        notification.save()
        CommonTestCases.admin_token_assert_equal(
          self,
          get_all_unread_notifications,
          get_all_unread_notifications_response_on_false
        )

    def test_change_notification_status(self):
        CommonTestCases.admin_token_assert_equal(
            self,
            change_notification_status_unexistent_id,
            change_notification_status_unexistent_id_response
        )
