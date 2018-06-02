from tests.base import BaseTestCase

from fixtures.floor.get_rooms_in_floor_fixtures import (
    get_rooms_in_floor, get_rooms_in_floor_response
)

import sys
import os
sys.path.append(os.getcwd())


class TestQueryFloorRooms(BaseTestCase):
    def test_query_rooms_in_floors(self):
        all_floors = self.client.execute(get_rooms_in_floor)
        self.assertEquals(all_floors, get_rooms_in_floor_response)
