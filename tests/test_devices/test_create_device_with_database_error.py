from tests.base import BaseTestCase
from helpers.database import engine, db_session
from fixtures.devices.devices_fixtures import (
    devices_query,
)

from fixtures.token.token_fixture import ADMIN_TOKEN

import sys
import os
sys.path.append(os.getcwd())


class TestCreateDevice(BaseTestCase):
    def test_create_device_connection_error(self):
        """
        test a user friendly message is returned to a user when database
        cannot be reached
        """
        db_session.remove()
        with engine.begin() as conn:
            conn.execute("DROP TABLE locations CASCADE")
            conn.execute("DROP TABLE devices CASCADE")
        headers = {"Authorization": "Bearer" + " " + ADMIN_TOKEN}
        query = self.app_test.post(devices_query, headers=headers)
        self.assertIn(
            "There seems to be a database connection error", str(query.data))
