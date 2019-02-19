from tests.base import BaseTestCase, CommonTestCases
from helpers.database import db_session, engine
from fixtures.room_resource.update_resource_fixtures import (
    update_room_resource_query,
)

import os
import sys
sys.path.append(os.getcwd())


class TestUpdateRoomResorce(BaseTestCase):

    def test_update_resource_without_resourse_model(self):
        db_session.remove()
        with engine.begin() as conn:
            conn.execute("DROP TABLE resources CASCADE")
        CommonTestCases.admin_token_assert_in(
            self,
            update_room_resource_query,
            "There seems to be a database connection error"
        )
