import sys
import os
from tests.base import BaseTestCase, CommonTestCases
from fixtures.wing.wing_fixtures import (
    create_wing_mutation, create_wing_mutation_response,
    duplicate_wing_mutation,
    duplicate_wing_mutation_response,
    wing_creation_no_name,
    wing_creation_no_name_response,
    create_wing_other_location,
    create_wing_other_location_admin,
    create_wing_floor_not_found
)

sys.path.append(os.getcwd())


class TestCreateWing(BaseTestCase):

    def test_wing_creation(self):
        """
        Testing for wing creation
        """
        CommonTestCases.lagos_admin_token_assert_equal(
            self,
            create_wing_mutation,
            create_wing_mutation_response
        )

    def test_wing_duplication(self):
        """
        Testing for wing duplication
        """
        CommonTestCases.lagos_admin_token_assert_equal(
            self,
            duplicate_wing_mutation,
            duplicate_wing_mutation_response
        )

    def test_wing_creation_no_name(self):
        """
        Testing for wing creation with no name
        """
        CommonTestCases.lagos_admin_token_assert_equal(
            self,
            wing_creation_no_name,
            wing_creation_no_name_response
        )

    def test_create_wing_other_location(self):
        """
        Testing for wing creation by admin in other location
        """
        CommonTestCases.admin_token_assert_in(
            self,
            create_wing_other_location,
            "This action is restricted to Lagos Office only"
        )

    def test_create_wing_lagos_admin_other_location(self):
        """
        Testing for wing creation in other Location by Lagos Admin
        """
        CommonTestCases.lagos_admin_token_assert_in(
            self,
            create_wing_other_location,
            "This action is restricted to Lagos Office only"
        )

    def test_create_wing_in_lagos_non_lagos_admin(self):
        """
        Testing for wing creation in other Location by Lagos Admin
        """
        CommonTestCases.admin_token_assert_in(
            self,
            create_wing_other_location_admin,
            "This action is restricted to Lagos Office admin"
        )

    def test_create_wing_floor_notfound(self):
        """
        Testing for wing creation when floor is not found
        """
        CommonTestCases.lagos_admin_token_assert_in(
            self,
            create_wing_floor_not_found,
            "Floor not found"
        )
