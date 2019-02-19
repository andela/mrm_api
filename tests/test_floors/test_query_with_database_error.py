from tests.base import BaseTestCase

from helpers.database import engine, db_session
from fixtures.floor.get_floors_fixures import (
    get_all_floors_query,
    paginated_floors_query,
)

import sys
import os
sys.path.append(os.getcwd())


class TestQueryFloors(BaseTestCase):
    def test_query_paginated_floors_with_database_error(self):
        db_session.remove()
        with engine.begin() as conn:
            conn.execute("DROP TABLE locations CASCADE")
            conn.execute("DROP TABLE floors CASCADE")
        paginated_floors = self.client.execute(paginated_floors_query)
        self.assertIn(
            "There seems to be a database connection error",
            str(paginated_floors))

    def test_query_all_floors_with_database_error(self):
        db_session.remove()
        with engine.begin() as conn:
            conn.execute("DROP TABLE locations CASCADE")
            conn.execute("DROP TABLE floors CASCADE")
        all_floors = self.client.execute(get_all_floors_query)
        self.assertIn(
            "There seems to be a database connection error", str(all_floors))
