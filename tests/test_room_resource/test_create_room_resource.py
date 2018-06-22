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

    def test_resource_creation_mutation_when_not_admin(self):

        api_headers = {'token': api_token}
        response = self.app_test.post('/mrm?query='+resource_mutation_query,
                                      headers=api_headers)
        self.assertIn("You are not authorized to perform this action",
                      str(response.data))

    def test_room_resource_creation_when_admin(self):
        email="patrick.walukagga@andela.com",
            location="Kampala")
        user.save()
        role = Role(role="Admin")
        role.save()
        user_role = UsersRole(user_id=user.id, role_id=role.id)
        user_role.save()
        role = Role(role="Default User")
        role.save()
        api_headers = {'token': api_token}
        response = self.app_test.post('/mrm?query='+resource_mutation_query,
                                      headers=api_headers)
        self.assertIn("Speakers", str(response.data))
