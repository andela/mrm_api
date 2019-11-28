from tests.base import BaseTestCase, CommonTestCases
from fixtures.user.user_fixture import (
    change_user_location_valid_input_mutation,
    change_user_location_invalid_user_mutation,
    change_user_location_invalid_location_id_mutation,
    change_user_location_to_same_location_mutation
)
from fixtures.user.user_fixture_response import (
    change_user_location_to_same_location_response,
    change_user_location_invalid_location_id_response,
    change_user_location_invalid_user_response,
    change_user_location_valid_input_response
)


class TestChangeUserLocation(BaseTestCase):

    def test_change_user_location_valid_input(self):
        """
        Test to change the location of a user with valid email and location_id
        """
        CommonTestCases.admin_token_assert_equal(
            self, change_user_location_valid_input_mutation,
            change_user_location_valid_input_response
        )

    def test_change_user_location_invalid_user(self):
        """
        Test that the supplied email must be for an existing user
        """
        CommonTestCases.admin_token_assert_equal(
            self, change_user_location_invalid_user_mutation,
            change_user_location_invalid_user_response
        )

    def test_change_user_location_invalid_location_id(self):
        """
        Test that the supplied location must exist in the database
        """
        CommonTestCases.admin_token_assert_equal(
            self, change_user_location_invalid_location_id_mutation,
            change_user_location_invalid_location_id_response
        )

    def test_change_user_location_same_location(self):
        """
        Test that the supplied location must be different from the user's
        current location
        """
        CommonTestCases.admin_token_assert_equal(
            self, change_user_location_to_same_location_mutation,
            change_user_location_to_same_location_response
        )
