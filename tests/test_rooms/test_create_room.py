import sys
import os
from tests.base import BaseTestCase, CommonTestCases
from fixtures.helpers.decorators_fixtures import (
    query_string, query_string_response
)
from fixtures.room.create_room_fixtures import (
    room_name_empty_mutation, room_invalid_officeId_mutation,
    room_invalid_floorId_mutation, room_invalid_wingId_mutation,
    room_mutation_query_duplicate_name,
    room_mutation_query_duplicate_name_response,
    room_invalid_calendar_id_mutation_query,
    room_invalid_calendar_id_mutation_response)
from fixtures.room.create_room_in_block_fixtures import (
    room_blockId_not_required_mutation
    )
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

    def test_room_creation_with_invalid_officeId(self):
        """
        Test room creation with  invalid officeId
        """
        CommonTestCases.admin_token_assert_in(
            self,
            room_invalid_officeId_mutation,
            "Office Id does not exist"
        )

    def test_room_creation_with_invalid_floorId(self):
        """
        Test room creation with  invalid floorId
        """
        CommonTestCases.admin_token_assert_in(
            self,
            room_invalid_floorId_mutation,
            "Floor Id does not exist"
        )

    def test_room_creation_with_invalid_wingId(self):
        """
        Test room creation with  invalid wingId
        """
        CommonTestCases.admin_token_assert_in(
            self,
            room_invalid_wingId_mutation,
            "Wing Id does not exist"
        )

    def test_room_creation_with_duplicate_name(self):
        """
        Test room creation with an already existing room name
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            room_mutation_query_duplicate_name,
            room_mutation_query_duplicate_name_response
        )

    def test_room_creation_when_blockId_not_required(self):
        """
        Test room creation with Block ID not required
        """
        CommonTestCases.admin_token_assert_in(
            self,
            room_blockId_not_required_mutation,
            "Block ID is not required for this office"
        )

    def test_room_creation_with_invalid_calendar_id(self):
        """
        Test room creation with Block ID not required
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            room_invalid_calendar_id_mutation_query,
            room_invalid_calendar_id_mutation_response
        )
