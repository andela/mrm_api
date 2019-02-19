from tests.base import BaseTestCase
from fixtures.role.role_fixtures import (
    role_query,
    query_role_by_role,
)
from helpers.database import db_session, engine
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

        db_session.remove()
        with engine.begin() as conn:
            conn.execute("DROP TABLE locations CASCADE")
            conn.execute("DROP TABLE roles CASCADE")
        execute_query = self.client.execute(
            role_query,
            context_value={'session': db_session})

        self.assertIn(
            "There seems to be a database connection error", str(execute_query))

    def test_query_role_by_role(self):
        role = Role(role='Ops')
        role.save()
        db_session().commit()

        db_session.remove()
        with engine.begin() as conn:
            conn.execute("DROP TABLE locations CASCADE")
            conn.execute("DROP TABLE roles CASCADE")
        execute_query = self.client.execute(
            query_role_by_role,
            context_value={'session': db_session})

        self.assertIn(
            "There seems to be a database connection error", str(execute_query))
