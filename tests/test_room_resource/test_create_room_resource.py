from tests.base import BaseTestCase, CommonTestCases
from fixtures.room_resource.room_resource_fixtures import (
    resource_mutation_query,
    resource_mutation_empty_name
)

import sys
import os
sys.path.append(os.getcwd())


class TestCreateRoomResource(BaseTestCase):

    def test_resource_creation_mutation_when_not_admin(self):
        CommonTestCases.user_token_assert_in(
            self,
            resource_mutation_query,
            "You are not authorized to perform this action"
        )

    def test_room_resource_creation_when_admin(self):
        CommonTestCases.admin_token_assert_in(
            self,
            resource_mutation_query,
            "Speakers"
        )

    def test_room_resource_creation_name_error(self):
        CommonTestCases.admin_token_assert_in(
            self,
            resource_mutation_empty_name,
            "name is required"
        )
