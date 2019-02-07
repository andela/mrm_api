import os
import sys

from tests.base import BaseTestCase
from fixtures.room.create_room_fixtures import (
    room_mutation_query)

sys.path.append(os.getcwd())


class TestAuthentication(BaseTestCase):
    def test_invalid_token_returns_error_message(self):
        """
        Test that an error message is returned when a user
        has an invalid token
        """
        headers = {"Authorization": "Bearer" + " " + "INVALID_TOKEN"}
        response = self.app_test.post(
            '/mrm?query=' + room_mutation_query,
            headers=headers)
        self.assertIn("Invalid token. Please Provide a valid token!",
                      str(response.data))
