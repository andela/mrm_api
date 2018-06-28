from tests.base import BaseTestCase
from fixtures.user_role.user_role_fixtures import (
    user_role_query, user_role_query_response,
    query_user_by_user_id, query_user_by_user_id_response
)
from helpers.database import db_session
from api.user.models import User
from api.role.models import Role
from api.user_role.models import UsersRole

import sys
import os
sys.path.append(os.getcwd())


class TestQueryUserRole(BaseTestCase):

    def test_query_users_role(self):
        """
        Testing for query User role
        """
        user = User(email="info@andela.com", location="Lagos")
        user.save()
        role = Role(role="Admin")
        role.save()
        user_role = UsersRole(user_id=1, role_id=1)
        user_role.save()
        db_session().commit()

        execute_query = self.client.execute(
            user_role_query,
            context_value={'session': db_session})

        expected_responese = user_role_query_response
        self.assertEqual(execute_query, expected_responese)

    def test_query_users_role_by_role(self):
        user = User(email='mrm@andela.com', location="Lagos")
        user.save()
        role = Role(role="Admin")
        role.save()
        user_role = UsersRole(user_id=1, role_id=1)
        user_role.save()
        db_session().commit()

        execute_query = self.client.execute(
            query_user_by_user_id,
            context_value={'session': db_session})

        expected_responese = query_user_by_user_id_response
        self.assertEqual(execute_query, expected_responese)
