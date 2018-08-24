from tests.base import BaseTestCase
from fixtures.room_resource.update_resource_fixtures import (
    update_room_resource_query,
    non_existant_resource_id_query
)
from fixtures.token.token_fixture import (admin_api_token, user_api_token)


import os
import sys
sys.path.append(os.getcwd())


class TestUpdateRoomResorce(BaseTestCase):

    def test_deleteresource_mutation_when_not_admin(self):

        api_headers = {'token': user_api_token}
        response = self.app_test.post(
            '/mrm?query=' +
            update_room_resource_query,
            headers=api_headers)
        self.assertIn("You are not authorized to perform this action",
                      str(response.data))

    def test_updateresource_mutation_when_admin(self):
        api_headers = {'token': admin_api_token}
        response = self.app_test.post(
            '/mrm?query=' +
            update_room_resource_query,
            headers=api_headers)
        self.assertIn("Markers", str(response.data))

    def test_updateresource_mutation_when_id_doesnt_exist(self):
        api_headers = {'token': admin_api_token}
        response = self.app_test.post(
            '/mrm?query=' +
            non_existant_resource_id_query,
            headers=api_headers)
        self.assertIn("Resource not found", str(response.data))
