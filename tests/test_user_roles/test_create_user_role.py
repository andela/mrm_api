from tests.base import BaseTestCase
from fixtures.user_role.user_role_fixtures import (
    user_role_mutation_query,
    user_role_mutation_response,
    user_mutation_query_for_duplicated_role,
)
from helpers.database import db_session
from api.user.models import User
import sys
import os
sys.path.append(os.getcwd())


def create_user():
    user = User(email="info@andela.com", location="Lagos",
                name="test test",
                picture="www.andela.com/test")
    user.save()
    db_session().commit()


class TestCreateUserRole(BaseTestCase):

    def test_user_role_creation(self):
        """
        Testing for User Role creation
        """

        create_user()

        execute_query = self.client.execute(
            user_role_mutation_query,
            context_value={'session': db_session})

        expected_response = user_role_mutation_response
        self.assertEqual(execute_query, expected_response)

    def test_user_role_duplication(self):
        """
        This test that one user can't be assigned two different roles
        """
        create_user()
        use_query = self.client.execute(
            user_mutation_query_for_duplicated_role,
            context_value={'session': db_session})

        self.assertIn(
            "This user is already assigned a role",
            str(use_query)
            )
