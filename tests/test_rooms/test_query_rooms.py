import json
import os
from unittest.mock import patch
from tests.base import BaseTestCase, CommonTestCases
from helpers.calendar.calendar import get_calendar_list_mock_data
from fixtures.room.create_room_query_fixtures import rooms_query
from fixtures.room.create_room_responses_fixtures import query_rooms_response
from fixtures.room.query_room_fixtures import (
    paginated_rooms_query,
    paginated_rooms_response,
    room_query_by_id,
    room_query_by_id_response,
    room_with_non_existant_id,
    room_query_with_non_existant_id_response,
    all_remote_rooms_query,
    paginated_rooms_query_blank_page,
    all_dummy_rooms_response
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
    @patch.dict(os.environ, {"APP_SETTINGS": "production"})
    def test_query_actual_remote_rooms(self, mock_get_json):
        """
           Mocks google calendar to return actual rooms
           on the production enviroment.
           Returns:
           - Actual rooms
           Actual rooms have no key words;
           - Test or Dummy
        """
        CommonTestCases.admin_token_assert_in(
            self,
            all_remote_rooms_query,
            "calendar.google.com"
        )

    @patch("api.room.schema_query.get_google_api_calendar_list", spec=True,
           return_value=get_calendar_list_mock_data())
    def test_query_test_remote_rooms(self, mock_get_json):
        """
           Mocks google calendar to return test rooms
           on the staging enviroment.
           Returns:
           - Test rooms
           Test rooms have the key words;
           - Test or Dummy
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            all_remote_rooms_query,
            all_dummy_rooms_response
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
