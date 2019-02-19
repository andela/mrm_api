from tests.base import BaseTestCase, CommonTestCases
from helpers.database import engine, db_session
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

    def test_get_user_notification_invalid_user(self):
        db_session.remove()
        with engine.begin() as conn:
            conn.execute("DELETE FROM users")

        CommonTestCases.admin_token_assert_in(
            self,
            user_notification_query,
            "User not found",
        )
