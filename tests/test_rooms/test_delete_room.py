from unittest.mock import patch
from tests.base import BaseTestCase, CommonTestCases

from fixtures.room.delete_room_fixtures import (
    delete_room_query,
    delete_room_query_non_existant_room_id,
)


class TestDeleteRoom(BaseTestCase):
    @patch('api.room.schema.subscriber.remove_room.delay')
    def test_delete_room_admin_user(self, mock_subscriber):
        mock_subscriber.return_value = True
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
