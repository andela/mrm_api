from tests.base import BaseTestCase, CommonTestCases
from helpers.database import engine, db_session
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

    def test_database_connection_error(self):
        """
        test a user friendly message is returned to a user when database
        cannot be reached
        """
        BaseTestCase().tearDown()
        CommonTestCases.admin_token_assert_in(
            self,
            delete_tag_query,
            "The database cannot be reached"
            )

    def test_delete_tag_without_tags_model(self):
        """
        Test if a user can create a tag when tags model is missing
        """
        db_session.remove()
        with engine.begin() as conn:
            conn.execute("DROP TABLE tags CASCADE")
        CommonTestCases.admin_token_assert_in(
            self,
            delete_tag_query,
            "does not exist")
