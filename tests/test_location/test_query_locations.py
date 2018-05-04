import sys
import os
sys.path.append(os.getcwd())
from os.path import dirname, abspath
mrm_api = dirname(dirname(abspath(__file__)))
sys.path.insert(0, mrm_api)

from tests.base import BaseTestCase

from fixtures.location.all_locations_fixtures import (
    all_locations_query,
    expected_query_all_locations
)
from fixtures.location.rooms_in_location_fixtures import (
    query_get_rooms_in_location,
    expected_query_get_rooms_in_location
)

from fixtures.location.nonexistant_location_id_fixtures import (
    query_nonexistant_location_id,
    expected_query_with_nonexistant_id
)

class QueryLocation(BaseTestCase):
    def test_query_all_locations(self):
        all_locations = self.client.execute(all_locations_query)
        self.assertEquals(all_locations, expected_query_all_locations)

    def test_query_rooms_in_a_location(self):
        get_room_in_a_location = self.client.execute (query_get_rooms_in_location)
        self.assertEquals(get_room_in_a_location,expected_query_get_rooms_in_location) 

    def test_query_rooms_in_a_location_with_nonexistant_id(self):
        query_with_wrong_id = self.client.execute(query_nonexistant_location_id)
        self.assertEquals(query_with_wrong_id , expected_query_with_nonexistant_id) 
                            
