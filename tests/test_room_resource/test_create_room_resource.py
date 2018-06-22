from tests.base import BaseTestCase
from fixtures.room_resource.room_resource_fixtures import (
    resource_mutation_query, resource_mutation_response,
    resource_mutation_0_value_room_id_query, error_0_value_room_id,
    resource_mutation_empty_name_string_query,
    resource_mutation_quantity_string_query, error_quantity_string
)
from fixtures.token.token_fixture import api_token
from api.user.models import User
from api.role.models import Role
from api.user_role.models import UsersRole

from helpers.database import db_session

import sys
import os
sys.path.append(os.getcwd())


class TestCreateRoomResource(BaseTestCase):

    def test_resource_additiom_mutation_when_not_admin(self):

        expected_responese = resource_mutation_response
        self.assertEqual(execute_query, expected_responese)

    def test_room_resource_creation_name_error(self):
        execute_query = resource_mutation_empty_name_string_query
        response = self.app_test.post('/mrm?query='+execute_query)
        self.assertIn("name is required field", str(response.data))

    def test_room_resource_creation_room_id_error(self):
        execute_query = self.client.execute(
            resource_mutation_0_value_room_id_query,
            context_value={'session': db_session})

        expected_responese = error_0_value_room_id
        self.assertEqual(execute_query, expected_responese)

    def test_room_resource_creation_quantity_error(self):
        execute_query = self.client.execute(
            resource_mutation_quantity_string_query,
            context_value={'session': db_session})

        expected_responese = error_quantity_string
        self.assertEqual(execute_query, expected_responese)
