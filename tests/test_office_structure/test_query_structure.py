from tests.base import BaseTestCase, CommonTestCases
from fixtures.office_structure.query_structure_fixture import (
    node_path_by_name_query,
    node_path_by_name_response,
    node_path_by_name_invalid_node_query
)


class TestQueryStructure(BaseTestCase):

    def test_node_path_by_name(self):
        """
        Test to get the full path of a node given the node_name
        """

        CommonTestCases.admin_token_assert_equal(
            self,
            node_path_by_name_query,
            node_path_by_name_response
        )

    def test_node_path_by_name_invalid_node(self):
        """
        Test to show that error will be returned if no node with
        provided node_name exists
        """

        CommonTestCases.admin_token_assert_in(
            self,
            node_path_by_name_invalid_node_query,
            "node not found"
        )
