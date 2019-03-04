from tests.base import BaseTestCase
from fixtures.user_role.user_role_fixtures import (
    user_role_mutation_query
)
from helpers.database import db_session, engine
from api.user.models import User

import sys
import os
sys.path.append(os.getcwd())


class TestCreateUserRole(BaseTestCase):
    def test_user_role_creation_without_users_model(self):
        """
        Test a user role cannot be created without a users model
        """
        user = User(email="info@andela.com", location="Lagos",
                    name="test test",
                    picture="www.andela.com/test")
        user.save()
        db_session().commit()

        db_session.remove()
        with engine.begin() as conn:
            conn.execute("DROP TABLE users CASCADE")
        execute_query = self.client.execute(
            user_role_mutation_query,
            context_value={'session': db_session})

        self.assertIn("The database cannot be reached", str(execute_query))
