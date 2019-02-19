

from tests.base import BaseTestCase, CommonTestCases
from helpers.database import db_session, engine
from fixtures.room.room_update_fixtures import (
    query_update_all_fields,
    query_without_room_id,
    query_room_id_non_existant,
    update_with_empty_field,
    response_for_update_room_with_database_error
)


class TestUpdateRoom(BaseTestCase):

    def test_resource_update_mutation_when_not_admin(self):
        CommonTestCases.user_token_assert_in(
            self,
            query_update_all_fields,
            "You are not authorized to perform this action")

    def test_if_all_fields_updated(self):
        CommonTestCases.admin_token_assert_in(
            self,
            query_update_all_fields,
            "Jinja")

    def test_for_error_if_id_not_supplied(self):
        CommonTestCases.admin_token_assert_in(
            self,
            query_without_room_id,
            "required positional argument")

    def test_for_error_if_room_id_is_non_existant_room(self):
        CommonTestCases.admin_token_assert_in(
            self,
            query_room_id_non_existant,
            "Room not found")

    def test_update_with_empty_field(self):
        CommonTestCases.admin_token_assert_in(
            self,
            update_with_empty_field,
            "name is required field")

    def test_database_connection_error(self):
        """
        test a user friendly message is returned to a user when database
        cannot be reached
        """
        BaseTestCase().tearDown()
        CommonTestCases.admin_token_assert_in(
            self,
            query_update_all_fields,
            "The database cannot be reached"
            )

    def test_update_room_without_rooms_model(self):
        db_session.remove()
        with engine.begin() as conn:
            conn.execute("DROP TABLE rooms CASCADE")
        CommonTestCases.admin_token_assert_equal(
            self,
            query_update_all_fields,
            response_for_update_room_with_database_error
        )
