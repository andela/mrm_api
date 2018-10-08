from tests.base import BaseTestCase, CommonTestCases
from fixtures.room_resource.update_resource_fixtures import (
    update_room_resource_query,
    non_existant_resource_id_query
)

import os
import sys
sys.path.append(os.getcwd())


class TestUpdateRoomResorce(BaseTestCase):

    def test_deleteresource_mutation_when_not_admin(self):
        CommonTestCases.user_token_assert_in(
            self,
            update_room_resource_query,
            "You are not authorized to perform this action"
        )

    def test_updateresource_mutation_when_admin(self):
        CommonTestCases.admin_token_assert_in(
            self,
            update_room_resource_query,
            "Markers"
        )

    def test_updateresource_mutation_when_id_doesnt_exist(self):
        CommonTestCases.admin_token_assert_in(
            self,
            non_existant_resource_id_query,
            "Resource not found"
        )
