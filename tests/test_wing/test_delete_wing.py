import sys
import os
from tests.base import BaseTestCase, CommonTestCases
from fixtures.wing.wing_fixtures import (
    delete_wing_mutation,
    delete_wing_id_not_found,
    delete_wing_response
)

sys.path.append(os.getcwd())


class TestCreateWing(BaseTestCase):

    def test_wing_deletion(self):
        """
        Testing for wing delete
        """
        CommonTestCases.lagos_admin_token_assert_equal(
            self,
            delete_wing_mutation,
            delete_wing_response
        )

    def test_wing_delete_other_location(self):
        """
        Testing for wing update in other location apart from Lagos
        """
        CommonTestCases.admin_token_assert_in(
            self,
            delete_wing_mutation,
            "This action is restricted to Lagos Office admin"
        )

    def test_delete_wing_id_notfound(self):
        """
        Testing for wing creation when floor is not found
        """
        CommonTestCases.lagos_admin_token_assert_in(
            self,
            delete_wing_id_not_found,
            "Wing not found"
        )
