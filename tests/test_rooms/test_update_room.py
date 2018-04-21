

from tests.base import BaseTestCase

from fixtures.room.room_update_fixtures import (
    query_update_all_fields,
    expected_query_update_all_fields,
    query_update_only_required_field,
    expected_query_update_only_required_field,
    query_without_keyword_name,
    expected_query_without_keyword_name,
    query_if_name_is_existant_room,
    expected_query_if_name_is_existant_room

)

class TestUpdateRoom(BaseTestCase):
    # test if can change fields
    def test_if_all_fields_updated(self):

        test_update_all_fields = self.client.execute(query_update_all_fields)
        assert test_update_all_fields == expected_query_update_all_fields

    # test if you can edit only required field.We shall only require to update the name in this test.
    def test_update_for_only_required_fields(self):
        
        test_edit_only_required_field = self.client.execute(query_update_only_required_field)
        assert test_edit_only_required_field == expected_query_update_only_required_field

    # test if you get error once keyword 'name' is not supplied in update query
    def test_for_error_if_name_not_supplied(self):
        test_get_error_if_no_name = self.client.execute(query_without_keyword_name)

        assert test_get_error_if_no_name == expected_query_without_keyword_name

    # test if you get error once keyword 'name' supplied is of room that is none existant
    def test_for_error_if_name_is_existant_room(self):
        
        test_get_error_if_room_is_none_existant = self.client.execute(query_if_name_is_existant_room )
        assert test_get_error_if_room_is_none_existant  == expected_query_if_name_is_existant_room 

