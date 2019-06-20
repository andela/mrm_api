from tests.base import BaseTestCase, CommonTestCases
from fixtures.admin_notification.admin_notification_fixtures import (
  get_all_unread_notifications,
  get_all_unread_notifications_response,
  change_notification_status_unexistent_id,
  change_notification_status_unexistent_id_response
)


class TestDeleteTag(BaseTestCase):
    def test_get_all_notifications(self):
        CommonTestCases.admin_token_assert_equal(
          self,
          get_all_unread_notifications,
          get_all_unread_notifications_response
        )

    def test_change_notification_status(self):
        CommonTestCases.admin_token_assert_equal(
            self,
            change_notification_status_unexistent_id,
            change_notification_status_unexistent_id_response
        )
