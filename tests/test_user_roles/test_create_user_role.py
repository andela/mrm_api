from tests.base import BaseTestCase
from fixtures.user_role.user_role_fixtures import (
    user_role_mutation_query, user_role_mutation_response
)
from helpers.database import db_session
from api.user.models import User

import sys
import os
sys.path.append(os.getcwd())


class TestCreateUserRole(BaseTestCase):

    def test_user_role_creation(self):
        """
        Testing for User Role creation
        """
        user = User(email="info@andela.com", location="Lagos",
                    name="test test",
                    picture="www.andela.com/test")
        user.save()
        db_session().commit()

        execute_query = self.client.execute(
            user_role_mutation_query,
            context_value={'session': db_session})

        expected_responese = user_role_mutation_response
        self.assertEqual(execute_query, expected_responese)
