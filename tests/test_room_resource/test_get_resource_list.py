import sys
import os
import json

from tests.base import BaseTestCase, CommonTestCases
from fixtures.room_resource.get_room_resource_fixtures import (
    resource_query, resource_query_response,
    filter_unique_resources, filter_unique_resources_response,
    get_paginated_room_resources,
    get_paginated_room_resources_response,
    get_paginated_resources_past_page,
    get_paginated_resources_inexistent_page,
    get_resource_by_room_id,
    get_resource_by_room_id_response_by_admin,
    get_resource_by_non_existing_room_id
)
from fixtures.room.assign_resource_fixture import (
    assign_resource_mutation,
    assign_resource_mutation_response
    )
from helpers.database import db_session
from fixtures.token.token_fixture import USER_TOKEN

sys.path.append(os.getcwd())


class TestGetRoomResource(BaseTestCase):
    maxDiff = None

    def test_get_room_resource_list(self):

        execute_query = self.client.execute(
            resource_query,
            context_value={'session': db_session})

        expected_responese = resource_query_response
        self.assertEqual(execute_query, expected_responese)

    def test_get_unique_resources(self):
        headers = {"Authorization": "Bearer" + " " + USER_TOKEN}
        response = self.app_test.post(
            '/mrm?query='+filter_unique_resources, headers=headers)
        actual_response = json.loads(response.data)
        self.assertEquals(actual_response, filter_unique_resources_response)

    def test_get_paginated_responses(self):
        CommonTestCases.admin_token_assert_equal(
            self,
            get_paginated_room_resources,
            get_paginated_room_resources_response
        )

    def test_get_paginated_resources_in_empty_page(self):
        CommonTestCases.admin_token_assert_in(
            self,
            get_paginated_resources_past_page,
            "No more resources"
        )

    def test_get_paginated_response_with_inexistent_page(self):
        CommonTestCases.admin_token_assert_in(
            self,
            get_paginated_resources_inexistent_page,
            "No page requested"
        )

    def test_get_room_resource_by_room_id_by_admin(self):
        '''
            Test getting room resources for a valid roomId
            by an admin returns correct resources
        '''
        # assign resource to a room
        CommonTestCases.admin_token_assert_equal(
           self,
           assign_resource_mutation,
           assign_resource_mutation_response,
        )
        CommonTestCases.admin_token_assert_equal(
            self,
            get_resource_by_room_id,
            get_resource_by_room_id_response_by_admin
        )

    def test_get_room_resource_by_invalid_room_id(self):
        '''
            Test that getting resource for non-existing roomId
            returns correct error message
        '''
        CommonTestCases.admin_token_assert_in(
            self,
            get_resource_by_non_existing_room_id,
            "Room not found"
        )

    def test_get_room_resource_by_room_id_by_non_admin(self):
        '''
            Test getting room resources for a valid roomId
            by a non admin returns correct message
        '''
        CommonTestCases.user_token_assert_in(
            self,
            get_resource_by_room_id,
            "You are not authorized to perform this action"
        )
