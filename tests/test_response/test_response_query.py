import sys
import os
from tests.base import BaseTestCase, CommonTestCases
from helpers.database import engine, db_session
from fixtures.response.room_response_fixture import (
   get_room_response_query,
)


sys.path.append(os.getcwd())


class TestRoomResponse(BaseTestCase):

    def test_room_response_with_no_feedback(self):
        """
        Testing for room response
        """
        db_session.remove()
        with engine.begin() as conn:
            conn.execute("DELETE FROM missing_items CASCADE")
            conn.execute("DELETE FROM responses CASCADE")
        CommonTestCases.admin_token_assert_in(
            self,
            get_room_response_query,
            "0"
        )

    def test_room_response_with_no_response_model(self):
        """
        Testing for room response
        """
        db_session.remove()
        with engine.begin() as conn:
            conn.execute("DROP TABLE missing_items CASCADE")
            conn.execute("DROP TABLE responses CASCADE")
        CommonTestCases.admin_token_assert_in(
            self,
            get_room_response_query,
            "error"
        )
