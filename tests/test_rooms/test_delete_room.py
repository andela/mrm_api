from tests.base import BaseTestCase, CommonTestCases

from helpers.database import db_session, engine
from fixtures.room.delete_room_fixtures import (
    delete_room_query,
    delete_room_query_non_existant_room_id,
    response_for_delete_room_with_database_error
)


class TestDeleteRoom(BaseTestCase):
    def test_delete_room_admin_user(self):
        CommonTestCases.admin_token_assert_in(
            self,
            delete_room_query,
            "Entebbe"
        )

    def test_delete_room_non_admin_user(self):
        CommonTestCases.user_token_assert_in(
            self,
            delete_room_query,
            "You are not authorized to perform this action"
        )

    def test_non_existant_room_id(self):
        CommonTestCases.admin_token_assert_in(
            self,
            delete_room_query_non_existant_room_id,
            "Room not found"
        )

    def test_database_connection_error(self):
        """
        test a user friendly message is returned to a user when database
        cannot be reached
        """
        BaseTestCase().tearDown()
        CommonTestCases.admin_token_assert_in(
            self,
            delete_room_query,
            "The database cannot be reached"
            )

    def test_delete_room_without_rooms_model(self):
        db_session.remove()
        with engine.begin() as conn:
            conn.execute("DROP TABLE rooms CASCADE")
        CommonTestCases.admin_token_assert_equal(
            self,
            delete_room_query,
            response_for_delete_room_with_database_error
        )
