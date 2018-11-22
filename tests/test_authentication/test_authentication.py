from tests.base import BaseTestCase
from fixtures.token.token_fixture import invalid_token
from fixtures.room.room_analytics_most_used_fixtures import (
    get_most_used_room_in_a_month_analytics_query)

import sys
import os
sys.path.append(os.getcwd())


class TestAuthentication(BaseTestCase):
    def test_invalid_token_returns_error_message(self):
        """
        Test that an error message is returned when a user
        has an invalid token
        """
        headers = {"Authorization": "Bearer" + " " + invalid_token}
        response = self.app_test.post(
            '/mrm?query=' + get_most_used_room_in_a_month_analytics_query,
            headers=headers)
        self.assertIn("invalid token", str(response.data))
