import sys
import os
from tests.base import BaseTestCase, CommonTestCases
from fixtures.wing.wing_fixtures import (
    query_all_wings,
    query_all_wings_response
)

sys.path.append(os.getcwd())


class TestCreateWing(BaseTestCase):

    def test_get_all_wings(self):
        """
        Testing for wing query
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            query_all_wings,
            query_all_wings_response
        )
