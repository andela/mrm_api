import sys
import os
from tests.base import BaseTestCase, CommonTestCases
from fixtures.helpers.decorators_fixtures import (
    tag_query_string, tag_query_string_response
)
from fixtures.room.create_room_with_tags_fixtures import (
    update_fields_mutation,
    update_fields_response,
    non_existing_tag_room_update,
    rooms_query,
    query_rooms_response,
    room_query_by_id,
    room_query_by_id_response
)
from fixtures.token.token_fixture import ADMIN_TOKEN

sys.path.append(os.getcwd())


class TestCreateRoomWithTags(BaseTestCase):

    def test_room_creation_with_tags(self):
        """
        Testing for room creation using tags
        """
        headers = {"Authorization": "Bearer" + " " + ADMIN_TOKEN}

        query = self.app_test.post(tag_query_string, headers=headers)
        expected_response = tag_query_string_response

        self.assertEqual(query.data, expected_response)

    def test_update_with_non_existant_tag(self):
        """
        Testing for room creation with inexistent tag
        """
        CommonTestCases.admin_token_assert_in(
            self,
            non_existing_tag_room_update,
            "Tag id 8 not found")

    def test_update_room_with_existant_tag(self):
        """
        Testing for room creation with existing tag
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            update_fields_mutation,
            update_fields_response)

    def test_query_room_with_tags(self):
        """
        Testing for room query
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            rooms_query,
            query_rooms_response)

    def test_query_room_by_id_with_tags(self):
        """
        Testing for room query
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            room_query_by_id,
            room_query_by_id_response)
