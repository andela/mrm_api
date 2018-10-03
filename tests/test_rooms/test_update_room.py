

from tests.base import BaseTestCase

from fixtures.room.room_update_fixtures import (
    query_update_all_fields,
    query_without_room_id,
    query_room_id_non_existant,
    update_with_empty_field
)
from fixtures.token.token_fixture import (user_api_token, admin_api_token)


class TestUpdateRoom(BaseTestCase):

    def test_resource_update_mutation_when_not_admin(self):
        headers = {"Authorization": "Bearer" + " " + user_api_token}
        response = self.app_test.post('/mrm?query='+query_update_all_fields,
                                      headers=headers)
        self.assertIn("You are not authorized to perform this action",
                      str(response.data))

    def test_if_all_fields_updated(self):
        headers = {"Authorization": "Bearer" + " " + admin_api_token}
        response = self.app_test.post('/mrm?query='+query_update_all_fields,
                                      headers=headers)
        self.assertIn("Jinja", str(response.data))

    def test_for_error_if_id_not_supplied(self):
        headers = {"Authorization": "Bearer" + " " + admin_api_token}
        response = self.app_test.post('/mrm?query='+query_without_room_id,
                                      headers=headers)
        self.assertIn("required positional argument", str(response.data))

    def test_for_error_if_room_id_is_non_existant_room(self):
        headers = {"Authorization": "Bearer" + " " + admin_api_token}
        response = self.app_test.post('/mrm?query='+query_room_id_non_existant,
                                      headers=headers)
        self.assertIn("Room not found", str(response.data))

    def test_update_with_empty_field(self):
        headers = {"Authorization": "Bearer" + " " + admin_api_token}
        response = self.app_test.post('/mrm?query='+update_with_empty_field,
                                      headers=headers)
        self.assertIn("name is required field", str(response.data))
