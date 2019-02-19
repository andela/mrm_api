from tests.base import BaseTestCase, CommonTestCases
from helpers.database import engine, db_session
from fixtures.location.create_location_fixtures import (
    create_location_query,
    response_for_create_location_with_database_error)

import sys
import os
sys.path.append(os.getcwd())


class TestCreateLocation(BaseTestCase):
    def test_create_location_without_location_relation(self):
        """
        Testing for floor creation without floor relation
        """
        db_session.remove()
        with engine.begin() as conn:
            conn.execute("DROP TABLE locations CASCADE")
        CommonTestCases.admin_token_assert_equal(
          self,
          create_location_query,
          response_for_create_location_with_database_error
        )
