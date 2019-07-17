from unittest.mock import patch
from tests.base import BaseTestCase
from helpers.room.subscriber import (add_room, remove_room, update_room_token)


class TestSubscriberTasks(BaseTestCase):

    @patch('helpers.room.subscriber.requests.get')
    def test_add_room(self, mock_get_request):
        """
        Test to verify that a request is made when
        the add_room function is called
        """
        add_room('calendar_id', 'firebase_token')
        mock_get_request.assert_called_once()

    @patch('helpers.room.subscriber.requests.delete')
    def test_remove_room(self, mock_delete_request):
        """
        Test to verify that a request is made when
        the remove_room function is called
        """
        remove_room('calendar_id')
        mock_delete_request.assert_called_once()

    @patch('helpers.room.subscriber.requests.get')
    def test_update_room_token(self, mock_get_request):
        """
        Test to verify that a request is made when
        the update_room_token function is called
        """
        update_room_token('calendar_id', 'firebase_token')
        mock_get_request.assert_called_once()
