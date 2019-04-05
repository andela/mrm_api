from tests.base import BaseTestCase, CommonTestCases
from fixtures.structure.structures_fixtures import (
    structures_query,
    expected_structures_query_response
)


class TestAllStructures(BaseTestCase):

    def test_query_all_structures_works(self):
        """
        Test that an admin is able to get all the office structures available
        """
        CommonTestCases.admin_token_assert_equal(
          self,
          structures_query,
          expected_structures_query_response
        )
