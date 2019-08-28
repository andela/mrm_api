from tests.base import BaseTestCase, CommonTestCases
from fixtures.office_structure.update_node_fixtures import (
    update_node_mutation,
    update_node_mutation_response,
    update_node_only_name_mutation,
    update_node_only_name_response,
    update_node_only_tag_mutation,
    update_node_empty_name_mutation,
    update_node_empty_tag_mutation,
    update_node_not_exist_mutation
)


class TestUpdateNode(BaseTestCase):
    def test_node_update(self):
        """
        Test that an Admin or Super Admnin can update a node
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            update_node_mutation,
            update_node_mutation_response
        )

    def test_only_name_node_update(self):
        """
        Test that only a name could be updated
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            update_node_only_name_mutation,
            update_node_only_name_response
        )

    def test_only_tag_node_update(self):
        """
        Test that only a tag could be updated
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            update_node_only_tag_mutation,
            update_node_mutation_response
        )

    def test_empty_name_update(self):
        """
        Test that an empty name is validated against
        """
        CommonTestCases.admin_token_assert_in(
            self,
            update_node_empty_name_mutation,
            "name is required field"
        )

    def test_empty_tag_update(self):
        """
        Test that an empty tag is validated against
        """
        CommonTestCases.admin_token_assert_in(
            self,
            update_node_empty_tag_mutation,
            "tag is required field"
        )

    def test_node_not_exist(self):
        """
        Test that the node to be updated exists before update attempt
        """
        CommonTestCases.admin_token_assert_in(
            self,
            update_node_not_exist_mutation,
            "node not found"
        )
