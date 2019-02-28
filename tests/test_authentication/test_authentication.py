import os
import sys

from tests.base import BaseTestCase
from fixtures.office.office_fixtures import (
    office_mutation_query)
from fixtures.token.token_fixture import INVALID_TOKEN

sys.path.append(os.getcwd())


class TestAuthentication(BaseTestCase):
    def test_invalid_token_returns_error_message(self):
        """
        Test that an error message is returned when a user
        has an invalid token
        """
        headers = {"Authorization": "Bearer" + " " + "INVALID_TOKEN"}
        response = self.app_test.post(
            '/mrm?query=' + office_mutation_query,
            headers=headers)
        self.assertIn("Invalid token. Please Provide a valid token!",
                      str(response.data))

    def test_unauthorised_token_returns_error_message(self):
        """
        Test that an error message is returned when a user
        has an unauthorised token
        """
        headers = {"Authorization": "Bearer" + " " + INVALID_TOKEN}
        response = self.app_test.post(
            '/mrm?query=' + office_mutation_query,
            headers=headers)
        self.assertIn("You are not authorized to perform this action",
                      str(response.data))
