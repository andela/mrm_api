from tests.base import BaseTestCase, CommonTestCases
from fixtures.tags.delete_tags_fixtures import (
  delete_tag_query,
  delete_tag_response,
  delete_non_existent_tag,
)


class TestDeleteTag(BaseTestCase):
    def test_delete_tag(self):
        CommonTestCases.admin_token_assert_equal(
          self,
          delete_tag_query,
          delete_tag_response
        )

    def test_delete_non_existent_tag(self):
        CommonTestCases.admin_token_assert_in(
          self,
          delete_non_existent_tag,
          "Tag not found"
        )
