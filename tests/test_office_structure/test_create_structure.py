from tests.base import BaseTestCase, CommonTestCases
from fixtures.office_structure.create_structure_fixtures import (
    valid_structure_mutation,
    valid_structure_mutation_response,
    structure_mutation_empty_node_list,
    structure_mutation_duplicate_node_id,
    structure_mutation_node_id_in_use,
    structure_mutation_multiple_root_nodes,
    structure_mutation_node_before_parent
)


class TestCreateStructure(BaseTestCase):

    def test_create_structure_valid_nodes(self):
        """
        Test to show that an admin can create a structure by supplying
        a valid node list
        """

        CommonTestCases.admin_token_assert_equal(
            self,
            valid_structure_mutation,
            valid_structure_mutation_response
        )

    def test_create_structure_empty_node_list(self):
        """
        Test to show that a structure cannot be created with an empty node list
        """

        CommonTestCases.admin_token_assert_in(
            self,
            structure_mutation_empty_node_list,
            "node_list cannot be empty"
        )

    def test_create_structure_duplicate_node_id(self):
        """
        Test to show that a structure cannot be created with duplicate
        node id in node list
        """

        CommonTestCases.admin_token_assert_in(
            self,
            structure_mutation_duplicate_node_id,
            "nodes must have unique id"
        )

    def test_create_structure_node_id_in_use(self):
        """
        Test to show that a structure cannot be created with node id in use
        """

        CommonTestCases.admin_token_assert_in(
            self,
            structure_mutation_node_id_in_use,
            'node id \\\\"c56a4180-65aa-42ec-a945-5fd21dec0518\\\\" in use'
        )

    def test_create_structure_multiple_root_nodes(self):
        """
        Test to show that a structure cannot be created with multiple root nodes
        """

        CommonTestCases.admin_token_assert_in(
            self,
            structure_mutation_multiple_root_nodes,
            "there must be exactly 1 root node. 2 were supplied"
        )

    def test_create_structure_node_appear_before_parent(self):
        """
        Test to show that a structure cannot be created if a node appears
        before its parent in the node list
        """

        CommonTestCases.admin_token_assert_in(
            self,
            structure_mutation_node_before_parent,
            'node \\\\"Ubuntu\\\\" appears before its parent'
        )
