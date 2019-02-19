from tests.base import BaseTestCase
from helpers.database import engine, db_session
from fixtures.role.role_fixtures import (
    role_mutation_query, role_mutation_response,
    role_duplication_mutation_response,
    create_role_with_database_error_response
)
import sys
import os
import pprint
sys.path.append(os.getcwd())


class TestCreateRole(BaseTestCase):

    def test_role_creation(self):
        """
        Testing for Role creation
        """
        execute_query = self.client.execute(
            role_mutation_query,
            context_value={'session': db_session})

        expected_responese = role_mutation_response
        self.assertEqual(execute_query, expected_responese)

    def test_role_duplication(self):
        """
        Testing for creation of an already existing role
        """
        self.client.execute(role_mutation_query,
                            context_value={'session': db_session})
        # Try to create a role twice
        query_response = self.client.execute(
            role_mutation_query, context_value={'session': db_session})

        expected_responese = role_duplication_mutation_response
        self.assertEqual(query_response, expected_responese)

    def test_role_creation_with_database_error(self):
        """
        Testing creation of roles with database
        """
        db_session.remove()
        with engine.begin() as conn:
            conn.execute("DROP TABLE roles CASCADE")
        execute_query = self.client.execute(
            role_mutation_query,
            context_value={'session': db_session})
        pprint.pprint(execute_query)
        self.assertEqual(
            create_role_with_database_error_response, execute_query)
