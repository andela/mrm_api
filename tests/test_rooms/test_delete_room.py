from tests.base import BaseTestCase

from fixtures.room.delete_room_fixtures import (
    delete_room_query,
    expected_response_room_query,
    delete_room_query_non_existant_room_id,
    expected_response_non_existant_room_id
)


class TestDeleteRoom(BaseTestCase):
    def test_delete_room(self):
        query = self.client.execute(delete_room_query)
        self.assertEquals(query, expected_response_room_query)

    def test_non_existant_room_id(self):
        query = self.client.execute(delete_room_query_non_existant_room_id)
        self.assertEquals(query, expected_response_non_existant_room_id)
