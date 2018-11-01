from tests.base import BaseTestCase, CommonTestCases
from fixtures.notification.notification_fixture import (
    user_notification_query,
    user_notification_response,
    update_user_notification_settings_query,
    update_user_notification_settings_response)

import sys
import os
sys.path.append(os.getcwd())


class TestNotification(BaseTestCase):

    def test_get_user_notification_(self):

        CommonTestCases.admin_token_assert_equal(
            self,
            user_notification_query,
            user_notification_response,
        )

    def test_update_user_notification_settings(self):

        CommonTestCases.admin_token_assert_equal(
            self,
            update_user_notification_settings_query,
            update_user_notification_settings_response,
        )
