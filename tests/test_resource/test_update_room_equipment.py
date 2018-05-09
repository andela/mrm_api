import os
import sys
sys.path.append(os.getcwd())

from os.path import dirname, abspath
mrm_api = dirname(dirname(abspath(__file__)))
sys.path.insert(0, mrm_api)

from tests.base import BaseTestCase
from fixtures.resource.update_resource_fixtures import (
    update_room_resource_query,
    expected_update_room_resource_query,
    non_existant_room_id_query,
    expected_non_existant_room_id_query,
    non_existant_resource_id_query,
    expected_non_existant_resource_id_query
)

class UpdateRoomResorce(BaseTestCase):
    def test_update_resource(self):
        """
        Test update resource with correct input. 
        """
        query = self.client.execute(update_room_resource_query)
        assert query == expected_update_room_resource_query

    def test_nonexistant_room_id(self):
        """
        Test when non existant room_id has been provided
        """
        query = self.client.execute(non_existant_room_id_query)
        assert query == expected_non_existant_room_id_query

    def test_nonexistant_resource_id(self):
        """
        Test when non existant resource_id has been provided
        """
        query = self.client.execute(non_existant_resource_id_query)
        assert query == expected_non_existant_resource_id_query
