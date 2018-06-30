import sys
import os

from tests.base import BaseTestCase
from fixtures.room_resource.delete_room_resource import (  # noqa: F401
  delete_resource, expected_query_after_delete)  # noqa: F401
from helpers.database import db_session  # noqa: F401
from fixtures.token.token_fixture import (admin_api_token, user_api_token)


sys.path.append(os.getcwd())


class TestDeleteRoomResource(BaseTestCase):

    def test_deleteresource_mutation_when_not_admin(self):

        api_headers = {'token': user_api_token}
        response = self.app_test.post('/mrm?query='+delete_resource,
                                      headers=api_headers)
        self.assertIn("You are not authorized to perform this action",
                      str(response.data))

    def test_deleteresource_mutation_when_admin(self):
        api_headers = {'token': admin_api_token}
        response = self.app_test.post('/mrm?query='+delete_resource,
                                      headers=api_headers)
        self.assertIn("Markers", str(response.data))
