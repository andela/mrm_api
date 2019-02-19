from tests.base import BaseTestCase
from fixtures.user_role.user_role_fixtures import (
    user_role_mutation_query,
)
from helpers.database import db_session, engine
from api.user.models import User

import sys
import os
sys.path.append(os.getcwd())


class TestCreateUserRole(BaseTestCase):
    def test_create_user_role_with_wrong_mutation(self):
        """
        Testing for user role creation without role model
        """
        db_session.remove()
        with engine.begin() as conn:
            conn.execute("DROP TABLE roles CASCADE")
        user = User(email="info@andela.com", location="Lagos",
                    name="test test",
                    picture="www.andela.com/test")
        user.save()
        db_session().commit()

        execute_query = self.client.execute(
            user_role_mutation_query,
            context_value={'session': db_session})
        self.assertIn(
            "There seems to be a database connection error", str(execute_query))
