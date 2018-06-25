from tests.base import BaseTestCase
from fixtures.room_resource.update_resource_fixtures import (
    update_room_resource_query,
    non_existant_resource_id_query
)
from fixtures.token.token_fixture import api_token
from api.user.models import User
from api.role.models import Role
from api.user_role.models import UsersRole


import os
import sys
sys.path.append(os.getcwd())


class TestUpdateRoomResorce(BaseTestCase):

    def test_deleteresource_mutation_when_not_admin(self):

        api_headers = {'token': api_token}
        response = self.app_test.post(
            '/mrm?query=' +
            update_room_resource_query,
            headers=api_headers)
        self.assertIn("You are not authorized to perform this action",
                      str(response.data))

    def test_updateresource_mutation_when_admin(self):

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
            '/mrm?query=' +
            update_room_resource_query,
            headers=api_headers)
        self.assertIn("Markers", str(response.data))

    def test_updateresource_mutation_when_id_doesnt_exist(self):

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
            '/mrm?query=' +
            non_existant_resource_id_query,
            headers=api_headers)
        self.assertIn("ResourceId not Found", str(response.data))
