import sys
import os

from tests.base import BaseTestCase
from fixtures.room_resource.get_room_resource_fixtures import (
    resource_query, get_room_resources_by_room_id,
    filter_unique_resources,
)
from helpers.database import db_session, engine
from fixtures.token.token_fixture import USER_TOKEN

sys.path.append(os.getcwd())


class TestGetRoomResource(BaseTestCase):
    def test_get_room_resource_list(self):
        db_session.remove()
        with engine.begin() as conn:
            conn.execute("DROP TABLE resources CASCADE")
        execute_query = self.client.execute(
            resource_query,
            context_value={'session': db_session})
        self.assertIn(
            "There seems to be a database connection error", str(execute_query))

    def test_get_room_resources_by_room_id(self):
        db_session.remove()
        with engine.begin() as conn:
            conn.execute("DROP TABLE resources CASCADE")
        execute_query = self.client.execute(
            get_room_resources_by_room_id,
            context_value={'session': db_session})
        self.assertIn(
            "relation \"resources\" does not exist", str(execute_query))

    def test_get_unique_resources(self):
        db_session.remove()
        with engine.begin() as conn:
            conn.execute("DROP TABLE resources CASCADE")
        headers = {"Authorization": "Bearer" + " " + USER_TOKEN}
        response = self.app_test.post(
            '/mrm?query='+filter_unique_resources, headers=headers)
        self.assertIn(
            "There seems to be a database connection error", str(response.data))
