from tests.base import BaseTestCase, CommonTestCases
from fixtures.office_structure.delete_level_fixtures import (
  delete_level_fixtures, delete_level_response,
  delete_level_fixtures_non_existant_id
)


class TestDeleteLevel(BaseTestCase):
    def test_delete_level_works(self):
        """Test admin can delete level"""
        CommonTestCases.admin_token_assert_equal(
            self,
            delete_level_fixtures,
            delete_level_response
        )

    def test_delete_level_with_nonexistant_id(self):
        """Test admin cannot delete level with nonexistent id"""
        CommonTestCases.admin_token_assert_in(
            self,
            delete_level_fixtures_non_existant_id,
            "Level not found"
        )
