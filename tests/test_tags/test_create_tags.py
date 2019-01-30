from tests.base import BaseTestCase, CommonTestCases
from fixtures.tags.create_tags_fixtures import (
    create_tag_query,
    create_tag_response,
    create_duplicate_tag_response,
    create_tag_with_duplicate_name,
    create_tag_with_missing_argument,
    create_tag_missing_args_response)


class TestCreateTag(BaseTestCase):

    def test_tag_creation(self):
        """
        Testing for tag creation
        """
        CommonTestCases.admin_token_assert_equal(
            self, create_tag_query, create_tag_response)

    def test_create_tag_with_duplicate_name(self):
        """
        Testing for tag creation with duplicate name
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            create_tag_with_duplicate_name,
            create_duplicate_tag_response
        )

    def test_create_tag_missing_an_argument(self):
        """
        Testing for tag creation with duplicate name
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            create_tag_with_missing_argument,
            create_tag_missing_args_response
        )
