import sys
import os
sys.path.append(os.getcwd())

from graphene.test import Client

from tests.base import BaseTestCase
from fixtures.role.role_fixtures import (
   role_mutation_query, role_mutation_response
)
from helpers.database import db_session

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
