from tests.base import BaseTestCase

from fixtures.room.room_fixtures import (
    rooms_query,
    query_rooms_response,
    room_query_by_id,
    room_query_by_id_response,
    room_with_non_existant_id,
    room_query_with_non_existant_id_response

)
class QueryRooms(BaseTestCase):
    def test_query_rooms(self):
        query_rooms = self.client.execute(rooms_query)
        self.assertEquals(query_rooms,query_rooms_response)

    def test_query_room_with_id(self):
        query = self.client.execute(room_query_by_id)
        self.assertEquals(query ,room_query_by_id_response)

    def test_query_room_with_non_existant_id(self):
        query = self.client.execute(room_with_non_existant_id)
        self.assertEquals(query ,room_query_with_non_existant_id_response)

