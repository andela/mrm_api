

from tests.base import BaseTestCase, CommonTestCases

from fixtures.room.room_update_fixtures import (
    query_update_all_fields,
    query_without_room_id,
    query_room_id_non_existant,
    update_with_empty_field,
    query_update_without_structure_id
)


class TestUpdateRoom(BaseTestCase):

    def test_resource_update_mutation_when_not_admin(self):
        CommonTestCases.user_token_assert_in(
            self,
            query_update_all_fields,
            "You are not authorized to perform this action")

    def test_if_all_fields_updated(self):
        CommonTestCases.admin_token_assert_in(
            self,
            query_update_all_fields,
            "Jinja")

    def test_for_error_if_id_not_supplied(self):
        CommonTestCases.admin_token_assert_in(
            self,
            query_without_room_id,
            "required positional argument")

    def test_for_error_if_room_id_is_non_existant_room(self):
        CommonTestCases.admin_token_assert_in(
            self,
            query_room_id_non_existant,
            "Room not found")

    def test_update_with_empty_field(self):
        CommonTestCases.admin_token_assert_in(
            self,
            update_with_empty_field,
            "name is required field")

    def test_update_without_structure_id(self):
        """
        Tests one can update a room without
        providing structure id
        """
        CommonTestCases.admin_token_assert_in(
            self,
            query_update_without_structure_id,
            "Jinja")
