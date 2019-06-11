from tests.base import BaseTestCase, CommonTestCases
from fixtures.room_resource.room_resource_fixtures import (
    resource_mutation_query
)
from fixtures.room_resource.resource_fixture import (
    resource_query,
    blank_resource_query,
    resource_response,
    none_existing_resource_response,
    search_blank_name_response
)


class TestResourceByName(BaseTestCase):
    """
    Test that an admin can query to get
    a specific resource using resource name
    """
    def test_resource_by_name(self):
        CommonTestCases.admin_token_assert_in(
            self,
            resource_mutation_query,
            "Speakers"
        )

        CommonTestCases.admin_token_assert_equal(
            self,
            resource_query,
            resource_response
        )

    def test_none_existing_resource_name(self):
        CommonTestCases.admin_token_assert_equal(
            self,
            resource_query,
            none_existing_resource_response
        )

    def test_blank_resource_name(self):
        CommonTestCases.admin_token_assert_equal(
            self,
            blank_resource_query,
            search_blank_name_response
        )
