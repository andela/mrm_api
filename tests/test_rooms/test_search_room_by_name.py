import sys
import os
import json


from tests.base import BaseTestCase
from fixtures.room.query_room_fixtures import (
    room_search_by_name,
    room_search_by_name_response,
    room_search_by_empty_name,
    room_search_by_empty_name_response,
    room_search_by_invalid_name,
    room_search_by_invalid_name_response
)

from fixtures.token.token_fixture import (user_api_token)

sys.path.append(os.getcwd())


class SearchRoomsByName(BaseTestCase):
    def test_search_room_by_name(self):
        api_headers = {'token': user_api_token}
        search_room_query = self.app_test.post(
            '/mrm?query='+room_search_by_name, headers=api_headers)
        actual_response = json.loads(search_room_query.data)
        self.assertEquals(actual_response, room_search_by_name_response)

    def test_search_room_by_empty_name(self):
        api_headers = {'token': user_api_token}
        search_room_empty_query = self.app_test.post(
            '/mrm?query='+room_search_by_empty_name, headers=api_headers)
        actual_response = json.loads(search_room_empty_query.data)
        expected_response = room_search_by_empty_name_response
        self.assertEquals(
            actual_response["errors"][0]['message'], expected_response)

    def test_search_room_by_invalid_name(self):
        api_headers = {'token': user_api_token}
        search_room_by_invalid_name = self.app_test.post(
            '/mrm?query='+room_search_by_invalid_name, headers=api_headers)
        actual_response = json.loads(search_room_by_invalid_name.data)
        expected_response = room_search_by_invalid_name_response
        self.assertEquals(
            actual_response["errors"][0]['message'], expected_response)
