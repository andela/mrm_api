

from tests.base import BaseTestCase

from fixtures.room.room_update_fixtures import (
    query_update_all_fields,
    expected_query_update_all_fields,
    query_update_only_required_field,
    expected_query_update_only_required_field,
    query_without_room_id,
    expected_query_without_room_id,
    query_if_room_id_is_existant_room,
    expected_query_if_room_id_is_existant_room

)

class TestUpdateRoom(BaseTestCase):

    def test_if_all_fields_updated(self):
        """
        Test if you can update all fields
        """
        test_update_all_fields = self.client.execute(query_update_all_fields)
        assert test_update_all_fields == expected_query_update_all_fields

    def test_update_for_only_required_fields(self):
        """
        Test if you can edit only required field. We shall only require to update the name in this test.
        """ 
        test_edit_only_required_field = self.client.execute(query_update_only_required_field)
        assert test_edit_only_required_field == expected_query_update_only_required_field

    def test_for_error_if_id_not_supplied(self):
        """
         Test if you get error once  'room_id' is not supplied in update query
        """
        test_get_error_if_no_id = self.client.execute(query_without_room_id)
        assert test_get_error_if_no_id == expected_query_without_room_id

    def test_for_error_if_name_is_existant_room(self):
        """
        Test if you get error once keyvalue 'room_id' supplied is of room that is none existant
        """ 
        test_get_error_if_room_is_none_existant = self.client.execute(query_if_room_id_is_existant_room )
        assert test_get_error_if_room_is_none_existant  == expected_query_if_room_id_is_existant_room 

