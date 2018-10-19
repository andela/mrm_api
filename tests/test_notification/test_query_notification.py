from tests.base import BaseTestCase, CommonTestCases
from fixtures.notification.notification_fixture import (
    non_existent_user_notification_settings_query,
    non_existent_user_notification_settings_response,
    missing_user_notification_table_query,
    missing_user_notification_table_response,
    existing_user_notification_table_query,
    existing_user_notification_table_response,
    update_user_notification_settings_query,
    update_user_notification_settings_response)

import sys
import os
sys.path.append(os.getcwd())


class TestNotification(BaseTestCase):
    def test_non_existent_user_notification_settings(self):

        CommonTestCases.user_token_assert_equal(
            self,
            non_existent_user_notification_settings_query,
            non_existent_user_notification_settings_response,
        )

    def test_missing_user_notification_table(self):

        CommonTestCases.user_token_assert_equal(
            self,
            missing_user_notification_table_query,
            missing_user_notification_table_response,
        )

    def test_update_user_notification_settings(self):

        CommonTestCases.user_token_assert_equal(
            self,
            update_user_notification_settings_query,
            update_user_notification_settings_response,
        )

    def test_existing_user_notification_table(self):
        CommonTestCases.user_token_assert_equal(
            self,
            existing_user_notification_table_query,
            existing_user_notification_table_response,
        )
