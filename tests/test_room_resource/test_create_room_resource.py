from tests.base import BaseTestCase
from fixtures.room_resource.room_resource_fixtures import (
    resource_mutation_query,
    resource_mutation_0_room_id,
    resource_mutation_empty_name
)
from fixtures.token.token_fixture import api_token
from api.user.models import User
from api.role.models import Role
from api.user_role.models import UsersRole

# from api.room.models import Room

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

        user = User(email="patrick.walukagga@andela.com",
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

    def test_room_resource_creation_name_error(self):
        user = User(email="patrick.walukagga@andela.com",
                    location="Kampala")
        user.save()
        role = Role(role="Admin")
        role.save()
        user_role = UsersRole(user_id=user.id, role_id=role.id)
        user_role.save()
        role = Role(role="Default User")
        role.save()
        api_headers = {'token': api_token}
        response = self.app_test.post(
                                    '/mrm?query='+resource_mutation_empty_name,
                                    headers=api_headers)
        self.assertIn("name is required", str(response.data))

    def test_room_resource_creation_room_id_error(self):
        user = User(email="patrick.walukagga@andela.com",
                    location="Kampala")
        user.save()
        role = Role(role="Admin")
        role.save()
        user_role = UsersRole(user_id=user.id, role_id=role.id)
        user_role.save()
        role = Role(role="Default User")
        role.save()
        api_headers = {'token': api_token}
        response = self.app_test.post(
                                    '/mrm?query='+resource_mutation_0_room_id,
                                    headers=api_headers)
        self.assertIn("room_id is required", str(response.data))
