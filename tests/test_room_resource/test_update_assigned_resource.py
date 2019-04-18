from tests.base import BaseTestCase, CommonTestCases
from fixtures.room_resource.update_assigned_resource import (
    update_assigned_resource_query,
    non_existant_resource_id_query,
    expected_update_assigned_resource_query,
    update_with_negative_quantity
)

import os
import sys
sys.path.append(os.getcwd())


class TestUpdateRoomResorce(BaseTestCase):

    def test_update_assigned_resource_by_non_admin(self):
        CommonTestCases.user_token_assert_in(
            self,
            update_assigned_resource_query,
            "You are not authorized to perform this action"
        )

    def test_update_assigned_resource_by_admin(self):
        CommonTestCases.admin_token_assert_equal(
            self,
            update_assigned_resource_query,
            expected_update_assigned_resource_query
        )

    def test_update_assigned_resource_with_invalid_id(self):
        CommonTestCases.admin_token_assert_in(
            self,
            non_existant_resource_id_query,
            "Invalid room or resource id"
        )

    def test_update_assigned_resource_with_negative_quantity(self):
        CommonTestCases.admin_token_assert_in(
            self,
            update_with_negative_quantity,
            "Assigned quantity cannot be less than zero"
        )

