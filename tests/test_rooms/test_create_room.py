import sys
import os
import json
from tests.base import BaseTestCase
from fixtures.token.token_fixture import admin_api_token
from fixtures.helpers.decorators_fixtures import (
    query_string, query_string_response
    )
from fixtures.room.room_fixtures import (
    room_name_empty_mutation, room_invalid_officeId_mutation,
    room_invalid_floorId_mutation, room_invalid_wingId_mutation)


sys.path.append(os.getcwd())


class TestCreateRoom(BaseTestCase):

    def test_room_creation(self):
        """
        Testing for room creation
        """

        api_headers = {'token': admin_api_token}
        query = self.app_test.post(query_string, headers=api_headers)
        expected_response = query_string_response

        self.assertEqual(query.data, expected_response)

    def test_room_creation_with_name_empty(self):
        """
        Test room creation with name field empty
        """

        api_headers = {'token': admin_api_token}
        response = self.app_test.post(
            '/mrm?query='+room_name_empty_mutation, headers=api_headers)
        actual_response = json.loads(response.data)
        expected_response = "name is required field"
        self.assertEquals(
            actual_response["errors"][0]["message"], expected_response)

    def test_room_creation_with_invalid_officeId(self):
        """
        Test room creation with  invalid officeId
        """
        api_headers = {'token': admin_api_token}
        response = self.app_test.post(
            '/mrm?query='+room_invalid_officeId_mutation, headers=api_headers)
        actual_response = json.loads(response.data)
        expected_response = "Office Id does not exist"
        self.assertEquals(
            actual_response["errors"][0]["message"], expected_response)

    def test_room_creation_with_invalid_floorId(self):
        """
        Test room creation with  invalid floorId
        """
        api_headers = {'token': admin_api_token}
        response = self.app_test.post(
            '/mrm?query='+room_invalid_floorId_mutation, headers=api_headers)
        actual_response = json.loads(response.data)
        expected_response = "Floor Id does not exist"
        self.assertEquals(
            actual_response["errors"][0]["message"], expected_response)

    def test_room_creation_with_invalid_wingId(self):
        """
        Test room creation with  invalid wingId
        """
        api_headers = {'token': admin_api_token}
        response = self.app_test.post(
            '/mrm?query='+room_invalid_wingId_mutation, headers=api_headers)
        actual_response = json.loads(response.data)
        expected_response = "Wing Id does not exist"
        self.assertEquals(
            actual_response["errors"][0]["message"], expected_response)
