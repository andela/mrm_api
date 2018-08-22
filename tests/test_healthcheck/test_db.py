from tests.base import BaseTestCase

from graphene.test import Client
from healthcheck_schema import healthcheck_schema
from fixtures.room.create_room_fixtures import (
    db_rooms_query,
    db_rooms_query_response,
)


class QueryRooms(BaseTestCase):
    def test_db_rooms_query(self):
        self.base_url = 'https://127.0.0.1:5000/_healthcheck'
        self.client = Client(healthcheck_schema)
        query_rooms = self.client.execute(db_rooms_query)
        self.assertEquals(query_rooms, db_rooms_query_response)
