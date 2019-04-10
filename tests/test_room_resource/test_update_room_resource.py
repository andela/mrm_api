from tests.base import BaseTestCase, CommonTestCases
from fixtures.room_resource.update_resource_fixtures import (
    update_room_resource_query,
    non_existant_resource_id_query,
    update_room_resource_negative_amount_query
)
from fixtures.room_resource.room_resource_fixtures import (
    resource_mutation_negative_quantity_response
)

import os
import sys
sys.path.append(os.getcwd())


class TestUpdateRoomResorce(BaseTestCase):

    def test_updateresource_mutation_by_non_admin(self):
        CommonTestCases.user_token_assert_in(
            self,
            update_room_resource_query,
            "You are not authorized to perform this action"
        )

    def test_update_resource_mutation_by_admin(self):
        CommonTestCases.admin_token_assert_in(
            self,
            update_room_resource_query,
            "Markers"
        )

    def test_update_resource_mutation_with_invalid_resource_id(self):
        CommonTestCases.admin_token_assert_in(
            self,
            non_existant_resource_id_query,
            "Resource not found"
        )

    def test_database_connection_error(self):
        """
        test a user friendly message is returned to a user when database
        cannot be reached
        """
        BaseTestCase().tearDown()
        CommonTestCases.admin_token_assert_in(
            self,
            update_room_resource_query,
            "The database cannot be reached"
            )

    def test_update_resource_with_negative_quantity(self):
        CommonTestCases.admin_token_assert_in(
            self,
            update_room_resource_negative_amount_query,
            resource_mutation_negative_quantity_response
            )
