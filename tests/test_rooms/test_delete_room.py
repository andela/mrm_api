from tests.base import BaseTestCase

from fixtures.room.delete_room_fixtures import (
    delete_room_query,
    delete_room_query_non_existant_room_id,
)
from fixtures.token.token_fixture import (user_api_token, admin_api_token)


class TestDeleteRoom(BaseTestCase):
    def test_delete_room_admin_user(self):
        api_headers = {'token': admin_api_token}
        response = self.app_test.post('/mrm?query='+delete_room_query,
                                      headers=api_headers)
        self.assertIn("Entebbe", str(response.data))

    def test_delete_room_non_admin_user(self):
        api_headers = {'token': user_api_token}
        response = self.app_test.post('/mrm?query='+delete_room_query,
                                      headers=api_headers)
        self.assertIn("You are not authorized to perform this action",
                      str(response.data))

    def test_non_existant_room_id(self):
        api_headers = {'token': admin_api_token}
        response = self.app_test.post('/mrm?query='+delete_room_query_non_existant_room_id, # noqa : E501
                                      headers=api_headers)
        self.assertIn("RoomId not found", str(response.data))
