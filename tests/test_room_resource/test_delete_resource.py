import sys
import os

from tests.base import BaseTestCase
from fixtures.room_resource.delete_room_resource import (  # noqa: F401
  delete_resource, expected_query_after_delete, delete_non_existant_resource)  # noqa: E501
from helpers.database import db_session  # noqa: F401
from fixtures.token.token_fixture import (admin_api_token, user_api_token)


sys.path.append(os.getcwd())


class TestDeleteRoomResource(BaseTestCase):

    def test_deleteresource_mutation_when_not_admin(self):

        headers = {"Authorization": "Bearer" + " " + user_api_token}
        response = self.app_test.post('/mrm?query='+delete_resource,
                                      headers=headers)
        self.assertIn("You are not authorized to perform this action",
                      str(response.data))

    def test_deleteresource_mutation_when_admin(self):
        headers = {"Authorization": "Bearer" + " " + admin_api_token}
        response = self.app_test.post('/mrm?query='+delete_resource,
                                      headers=headers)
        self.assertIn("Markers", str(response.data))

    def test_non_existant_deleteresource_mutation(self):

        headers = {"Authorization": "Bearer" + " " + admin_api_token}
        response = self.app_test.post('/mrm?query='+delete_non_existant_resource,  # noqa: E501
                                      headers=headers)
        self.assertIn("Resource not found", str(response.data))
