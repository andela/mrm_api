from tests.base import BaseTestCase

from fixtures.room.room_fixtures import (
    rooms_query,
    query_rooms_response,
    room_query_by_id,
    room_query_by_id_response
)
class QueryRooms(BaseTestCase):
    def test_query_rooms(self):
        query_rooms = self.client.execute(rooms_query)
        assert query_rooms == query_rooms_response

    def test_query_room_with_id(self):
        query = self.client.execute(room_query_by_id)
        assert query == room_query_by_id_response 
