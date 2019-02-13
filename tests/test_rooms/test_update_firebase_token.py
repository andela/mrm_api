from tests.base import BaseTestCase
from fixtures.room.update_firebase_token_fixtures import (
    update_mutation,
    update_response,
    incorrect_room_id_mutation,
    update_with_empty_token
)
from helpers.database import db_session
import sys

import os
sys.path.append(os.getcwd())


class TestFirebaseToken(BaseTestCase):

    def test_update_firebase_token(self):
        """
        Testing successful token update
        """
        execute_query = self.client.execute(
            update_mutation,
            context_value={'session': db_session})

        expected_responese = update_response
        self.assertEqual(execute_query, expected_responese)

    def test_update_firebase_token_with_incorrect_id(self):
        """
        Testing for mutation with incorrect id
        """
        execute_query = self.client.execute(
            incorrect_room_id_mutation,
            context_value={'session': db_session})
        self.assertIn("Room not found", str(execute_query))

    def test_update_firebase_token_with_empty_token(self):
        """
        Testing for mutation with empty token
        """
        execute_query = self.client.execute(
            update_with_empty_token,
            context_value={'session': db_session})
        self.assertIn("firebase_token is required field", str(execute_query))
