from tests.base import BaseTestCase

from helpers.database import engine, db_session
from fixtures.location.all_locations_fixtures import (
    all_locations_query,
)
from fixtures.location.rooms_in_location_fixtures import (
    query_get_rooms_in_location,
)

import sys
import os
sys.path.append(os.getcwd())


class TestQueryLocation(BaseTestCase):
    def test_query_all_locations_without_location_model(self):
        db_session.remove()
        with engine.begin() as conn:
            conn.execute("DROP TABLE locations CASCADE")
            conn.execute("DROP TABLE floors CASCADE")
        all_locations = self.client.execute(all_locations_query)
        self.assertIn(
            "There seems to be a database connection error", str(all_locations))

    def test_query_rooms_in_a_location(self):
        db_session.remove()
        with engine.begin() as conn:
            conn.execute("DROP TABLE locations CASCADE")
            conn.execute("DROP TABLE floors CASCADE")
        get_room_in_a_location = self.client.execute(query_get_rooms_in_location)  # noqa: E501
        self.assertIn(
            "There seems to be a database connection error",
            str(get_room_in_a_location))
