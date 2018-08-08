import json

from tests.base import BaseTestCase
from fixtures.room.room_fixtures import (
    rooms_query,
    query_rooms_response,
    paginated_rooms_query,
    paginated_rooms_response,
    room_query_by_id,
    room_query_by_id_response,
    room_with_non_existant_id,
    room_query_with_non_existant_id_response

)


class QueryRooms(BaseTestCase):
    def test_query_rooms(self):
        execute_query = self.client.execute(
            rooms_query)
        expected_response = query_rooms_response
        self.assertEqual(execute_query, expected_response)

    def test_paginate_room_query(self):
        response = self.app_test.post('/mrm?query='+paginated_rooms_query)
        paginate_query = json.loads(response.data)
        expected_response = paginated_rooms_response
        self.assertEqual(paginate_query, expected_response)

    def test_query_room_with_id(self):
        query = self.client.execute(room_query_by_id)

        self.assertEquals(query, room_query_by_id_response)

    def test_query_room_with_non_existant_id(self):
        response = self.app_test.post('/mrm?query='+room_with_non_existant_id)
        actual_response = json.loads(response.data)
        expected_response = room_query_with_non_existant_id_response
        self.assertEquals(
            actual_response["errors"][0]['message'], expected_response)
