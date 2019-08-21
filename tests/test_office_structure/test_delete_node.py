from tests.base import BaseTestCase, CommonTestCases
from fixtures.office_structure.delete_office_structure_fixtures import (
    delete_node_by_id_mutation,
    delete_node_by_id_response,
    delete_node_invalid_id_mutation
)


class TestDeleteNode(BaseTestCase):

    def test_delete_node_by_id(self):
        """
        Tests to delete a node given the node id
        """

        CommonTestCases.admin_token_assert_equal(
            self,
            delete_node_by_id_mutation,
            delete_node_by_id_response
        )

    def test_delete_node_by_id_invalid_node_id(self):
        """
        Test to show that error will be returned if no node with
        provided node id exists
        """

        CommonTestCases.admin_token_assert_in(
            self,
            delete_node_invalid_id_mutation,
            "The specified node does not exist"
        )
