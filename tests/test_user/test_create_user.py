from tests.base import BaseTestCase
from fixtures.user.user_fixture import (
    user_mutation_query, user_mutation_response
)
from helpers.database import db_session

import sys
import os
sys.path.append(os.getcwd())


class TestCreateUser(BaseTestCase):

    def test_user_creation(self):
        """
        Testing for User creation
        """
        execute_query = self.client.execute(
            user_mutation_query,
            context_value={'session': db_session})

        expected_responese = user_mutation_response
        self.assertEqual(execute_query, expected_responese)
