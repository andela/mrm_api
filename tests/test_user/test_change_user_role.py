from tests.base import BaseTestCase, CommonTestCases
from fixtures.user.user_fixture import (
    change_user_role_mutation, change_user_role_mutation_response,
    change_user_role_to_non_existence_role_mutation,
    change_user_role_to_non_existing_role_mutation_response,
    change_role_of_non_existing_user_mutation,
    assign_role_to_non_existing_user_mutation
)

import sys
import os
sys.path.append(os.getcwd())


class TestChangeUserRole(BaseTestCase):

    def test_change_user_role(self):
        """
        Testing change of user role
        """
        CommonTestCases.admin_token_assert_equal(
            self, change_user_role_mutation, change_user_role_mutation_response
        )

    def test_change_user_role_with_non_existing_role_id(self):
        """
        Testing change of user role with non existing role_id
        """
        CommonTestCases.admin_token_assert_in(
            self, change_user_role_to_non_existence_role_mutation,
            change_user_role_to_non_existing_role_mutation_response
        )

    def test_changing_role_of_none_existing_user(self):
        """
        Testing change of user role of a non existing user
        """
        CommonTestCases.admin_token_assert_in(
            self,
            change_role_of_non_existing_user_mutation,
            "User not found"
        )

    def test_assign_role_to_none_existing_user(self):
        """
        Testing assign role to a non existing user
        """
        CommonTestCases.admin_token_assert_in(
            self,
            assign_role_to_non_existing_user_mutation,
            "User not found"
        )
