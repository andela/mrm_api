import sys
import os
from unittest.mock import patch

from tests.base import BaseTestCase, CommonTestCases
from fixtures.helpers.decorators_fixtures import (
    query_string, query_string_response
)
from fixtures.room.create_room_fixtures import (
    room_mutation_query,
    room_name_empty_mutation,
    room_mutation_query_duplicate_name,
    room_mutation_query_duplicate_name_response,
    room_invalid_calendar_id_mutation_query,
    room_duplicate_calender_id_mutation_query,
    room_duplicate_calendar_id_mutation_response,
    room_invalid_location_id_mutation,
    room_invalid_tag_mutation,
    invalid_room_label_query,
    non_existent_structure_room_label_query,
    room_mutation_query_response)
from fixtures.token.token_fixture import ADMIN_TOKEN

sys.path.append(os.getcwd())


class TestCreateRoom(BaseTestCase):

    def test_room_creation(self):
        """
        Testing for room creation
        """
        headers = {"Authorization": "Bearer" + " " + ADMIN_TOKEN}

        query = self.app_test.post(query_string, headers=headers)
        expected_response = query_string_response
        self.assertEqual(query.data, expected_response)

    def test_room_creation_with_name_empty(self):
        """
        Test room creation with name field empty
        """
        CommonTestCases.admin_token_assert_in(
            self,
            room_name_empty_mutation,
            "name is required field"
        )

    def test_room_creation_with_duplicate_name_in_the_same_location(self):
        """
        Test that room creation with duplicate room name in the same
        location will fail
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            room_mutation_query_duplicate_name,
            room_mutation_query_duplicate_name_response
        )

    def test_invalid_room_label_format(self):
        """
        Test that room label does not accepts list of
        dictionaries and saves them as strings
        """
        CommonTestCases.admin_token_assert_in(
            self,
            invalid_room_label_query,
            "Room label is not a valid string type")

    def test_valid_room_label_format(self):
        """
        Test when the room label inserted is valid
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            room_mutation_query,
            room_mutation_query_response)

    def test_nonexistent_structure_room_label_query(self):
        """
        Test that a room label cannot be created when
        structure does not exist
        """
        CommonTestCases.admin_token_assert_in(
            self,
            non_existent_structure_room_label_query,
            "Structure does not exist")

    def test_create_room_with_invalid_location_id(self):
        """
        Testing for room creation with invalid location id
        """
        CommonTestCases.admin_token_assert_in(
            self,
            room_invalid_location_id_mutation,
            "Location Id does not exist")

    def test_create_room_in_other_location(self):
        """
        Test for creation of room in s different location
        """
        CommonTestCases.lagos_admin_token_assert_in(
            self,
            room_mutation_query,
            "You are not authorized to make changes in Kampala"
        )

    def test_room_mutation_invalid_tag(self):
        """
        Test for creation of room with invalid tag
        """
        CommonTestCases.admin_token_assert_in(
            self,
            room_invalid_tag_mutation,
            "Tag id 8 not found"
        )

    @patch("api.room.models.verify_calendar_id",
           spec=True)
    def test_room_creation_with_invalid_calendar_id(self, mock_get_json):
        """
        Test room creation with invalid calendar id
        """
        mock_get_json.return_value = False
        CommonTestCases.admin_token_assert_in(
            self,
            room_invalid_calendar_id_mutation_query,
            "Room calendar Id is invalid"
        )

    def test_room_creation_with_invalid_duplicate_calendar_id(self):
        """
        Test room creation with a duplicate callender Id
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            room_duplicate_calender_id_mutation_query,
            room_duplicate_calendar_id_mutation_response
        )
