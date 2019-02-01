from tests.base import BaseTestCase
from fixtures.user.user_fixture import (
    user_mutation_query, user_mutation_response,
    user_duplication_mutation_response
)
from fixtures.user.add_user_fixture import (
    non_Andela_email_mutation,
    non_Andela_email_mutation_response
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

        expected_response = user_mutation_response
        self.assertEqual(execute_query, expected_response)

    def test_user_duplication(self):
        """
        Testing for creation of an already existing user
        """
        self.client.execute(user_mutation_query,
                            context_value={'session': db_session})
        # Try to create a user twice
        query_response = self.client.execute(
            user_mutation_query,
            context_value={'session': db_session})

        expected_response = user_duplication_mutation_response
        self.assertEqual(query_response, expected_response)

    def test_user_creation_with_non_andela_email(self):
        """
        Testing for adding a user with non Andela Email
        """
        query_response = self.client.execute(
            non_Andela_email_mutation,
            context_value={'session': db_session})
        self.assertEqual(query_response, non_Andela_email_mutation_response)
