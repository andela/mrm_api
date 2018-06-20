import sys
import os

from tests.base import BaseTestCase
from fixtures.room_resource.delete_room_resource import (  # noqa: F401
  delete_resource, expected_query_after_delete)  # noqa: F401
from helpers.database import db_session  # noqa: F401
from fixtures.token.token_fixture import api_token
from api.user.models import User
from api.role.models import Role
from api.user_role.models import UsersRole

sys.path.append(os.getcwd())


class TestDeleteRoomResource(BaseTestCase):

    def test_deleteresource_mutation_when_not_admin(self):

        api_headers = {'token': api_token}
        response = self.app_test.post('/mrm?query='+delete_resource,
                                      headers=api_headers)
        self.assertIn("You are not authorized to perform this action",
                      str(response.data))

    def test_deleteresource_mutation_when_admin(self):

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
        response = self.app_test.post('/mrm?query='+delete_resource,
                                      headers=api_headers)
        self.assertIn("Markers", str(response.data))
