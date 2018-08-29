

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
        api_headers = {'token': user_api_token}
        response = self.app_test.post('/mrm?query='+query_update_all_fields,
                                      headers=api_headers)
        self.assertIn("You are not authorized to perform this action",
                      str(response.data))

    def test_if_all_fields_updated(self):
        api_headers = {'token': admin_api_token}
        response = self.app_test.post('/mrm?query='+query_update_all_fields,
                                      headers=api_headers)
        self.assertIn("Jinja", str(response.data))

    def test_for_error_if_id_not_supplied(self):
        api_headers = {'token': admin_api_token}
        response = self.app_test.post('/mrm?query='+query_without_room_id,
                                      headers=api_headers)
        self.assertIn("required positional argument", str(response.data))

    def test_for_error_if_room_id_is_non_existant_room(self):
        api_headers = {'token': admin_api_token}
        response = self.app_test.post('/mrm?query='+query_room_id_non_existant,
                                      headers=api_headers)
        self.assertIn("Room not found", str(response.data))

    def test_update_with_empty_field(self):
        api_headers = {'token': admin_api_token}
        response = self.app_test.post('/mrm?query='+update_with_empty_field,
                                      headers=api_headers)
        self.assertIn("name is required field", str(response.data))
