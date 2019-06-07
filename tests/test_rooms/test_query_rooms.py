import json
from unittest.mock import patch
from tests.base import BaseTestCase, CommonTestCases
from helpers.calendar.calendar import get_calendar_list_mock_data
from fixtures.room.create_room_fixtures import (
    rooms_query,
    query_rooms_response)
from fixtures.room.query_room_fixtures import (
    paginated_rooms_query,
    paginated_rooms_response,
    room_query_by_id,
    room_query_by_id_response,
    room_with_non_existant_id,
    room_query_with_non_existant_id_response,
    all_remote_rooms_query,
    paginated_rooms_query_blank_page
)
from helpers.calendar.credentials import get_google_api_calendar_list


class QueryRooms(BaseTestCase):
    def test_query_rooms(self):
        execute_query = self.client.execute(
            rooms_query)
        expected_response = query_rooms_response
        self.assertEqual(execute_query, expected_response)

    def test_paginate_room_query(self):
        CommonTestCases.admin_token_assert_equal(
            self,
            paginated_rooms_query,
            paginated_rooms_response
        )

    @patch("api.room.schema_query.get_google_api_calendar_list", spec=True,
           return_value=get_calendar_list_mock_data())
    def test_query_remote_rooms(self, mock_get_json):
        CommonTestCases.admin_token_assert_in(
            self,
            all_remote_rooms_query,
            "calendar.google.com"
        )

    @patch("helpers.calendar.credentials.Credentials")
    def test_calendar_list_function(self, mocked_method):
        '''
            mock calender API service and
            test if it was called atleast once
        '''
        get_google_api_calendar_list()
        assert mocked_method.called

    def test_query_room_with_id(self):
        response = self.app_test.post('/mrm?query='+room_query_by_id)
        actual_response = json.loads(response.data)
        self.assertEquals(actual_response, room_query_by_id_response)

    def test_query_room_with_non_existant_id(self):
        response = self.app_test.post('/mrm?query='+room_with_non_existant_id)
        actual_response = json.loads(response.data)
        expected_response = room_query_with_non_existant_id_response
        self.assertEquals(
            actual_response["errors"][0]['message'], expected_response)

    def test_paginated_empty_page(self):
        CommonTestCases.admin_token_assert_in(
            self,
            paginated_rooms_query_blank_page,
            "No more resources"
        )
