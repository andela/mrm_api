

from tests.base import BaseTestCase

from fixtures.room.room_update_fixtures import (
    query_update_all_fields,
    expected_query_update_all_fields,
    query_update_only_required_field,
    expected_query_update_only_required_field,
    query_without_room_id,
    expected_query_without_room_id,
    query_if_room_id_is_non_existant_room,
    expected_query_if_room_id_is_non_existant_room,
    update_with_empty_field,
    expected_response_update_with_empty_field

)


class TestUpdateRoom(BaseTestCase):

    def test_if_all_fields_updated(self):
        """
        Test if you can update all fields
        """
        test_update_all_fields = self.client.execute(query_update_all_fields)
        self.assertEquals(test_update_all_fields, expected_query_update_all_fields)  # noqa: E501

    def test_update_for_only_required_fields(self):
        """
        Test if you can edit only required field.
        We shall only require to update the name in this test.
        """
        test_edit_only_required_field = self.client.execute(query_update_only_required_field)  # noqa: E501
        self.assertEquals(test_edit_only_required_field, expected_query_update_only_required_field)  # noqa: E501

    def test_for_error_if_id_not_supplied(self):
        """
         Test if you get error once  'room_id' is not supplied in update query
        """
        test_get_error_if_no_id = self.client.execute(query_without_room_id)
        self.assertEquals(test_get_error_if_no_id, expected_query_without_room_id)  # noqa: E501

    def test_for_error_if_room_id_is_non_existant_room(self):
        """
        Test if you get error once keyvalue 'room_id' supplied is
        of room that is non-existant
        """
        test_get_error_if_room_is_none_existant = self.client.execute(query_if_room_id_is_non_existant_room)  # noqa: E501
        self.assertEquals(test_get_error_if_room_is_none_existant, expected_query_if_room_id_is_non_existant_room)  # noqa: E501

    def test_update_with_empty_field(self):
        """
        test if you get error when you suppy and empty field for example
        and empty name string
        """
        query = self.client.execute(update_with_empty_field)
        self.assertEquals(query, expected_response_update_with_empty_field)
