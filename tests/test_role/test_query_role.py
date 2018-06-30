from tests.base import BaseTestCase
from fixtures.role.role_fixtures import (
    role_query, role_query_response,
    query_role_by_role, query_role_by_role_response
)
from helpers.database import db_session
from api.role.models import Role

import sys
import os
sys.path.append(os.getcwd())


class TestQueryRole(BaseTestCase):

    def test_query_role(self):
        """
        Testing for User creation
        """
        role = Role(role='Ops')
        role.save()
        db_session().commit()

        execute_query = self.client.execute(
            role_query,
            context_value={'session': db_session})

        expected_responese = role_query_response
        self.assertEqual(execute_query, expected_responese)

    def test_query_role_by_role(self):
        role = Role(role='Ops')
        role.save()
        db_session().commit()

        execute_query = self.client.execute(
            query_role_by_role,
            context_value={'session': db_session})

        expected_responese = query_role_by_role_response
        self.assertEqual(execute_query, expected_responese)
