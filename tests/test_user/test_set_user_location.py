from tests.base import BaseTestCase, CommonTestCases
from fixtures.user.user_fixture import (
    set_user_location_mutation,
    set_user_location_mutation_response,
    set_user_location_exists_mutation,
    set_location_for_user_with_location_response

)


class TestSetUserLocation(BaseTestCase):

    def test_set_user_location(self):
        """
        Test to set a location for a user with no location
        """
        CommonTestCases.lagos_admin_token_assert_equal(
            self, set_user_location_mutation,
            set_user_location_mutation_response
        )

    def test_set_user_location_when_location_exists(self):
        """
        Test to set a location for a user who already has a location
        """
        CommonTestCases.admin_token_assert_equal(
            self, set_user_location_exists_mutation,
            set_location_for_user_with_location_response
        )
