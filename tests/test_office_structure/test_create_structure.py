from tests.base import BaseTestCase, CommonTestCases
from fixtures.office_structure.create_structure_fixtures import (
    valid_structure_mutation,
    valid_structure_mutation_response,
    structure_mutation_empty_node_list,
    structure_mutation_empty_node_list_response,
    structure_mutation_duplicate_node_id,
    structure_mutation_duplicate_node_id_reponse,
    structure_mutation_node_id_in_use,
    structure_mutation_node_id_in_use_response,
    structure_mutation_multiple_root_nodes,
    structure_mutation_multiple_root_nodes_response,
    structure_mutation_node_before_parent,
    structure_mutation_node_before_parent_response
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

        CommonTestCases.admin_token_assert_equal(
            self,
            structure_mutation_empty_node_list,
            structure_mutation_empty_node_list_response
        )

    def test_create_structure_duplicate_node_id(self):
        """
        Test to show that a structure cannot be created with duplicate
        node id in node list
        """

        CommonTestCases.admin_token_assert_equal(
            self,
            structure_mutation_duplicate_node_id,
            structure_mutation_duplicate_node_id_reponse
        )

    def test_create_structure_node_id_in_use(self):
        """
        Test to show that a structure cannot be created with node id in use
        """

        CommonTestCases.admin_token_assert_equal(
            self,
            structure_mutation_node_id_in_use,
            structure_mutation_node_id_in_use_response
        )

    def test_create_structure_multiple_root_nodes(self):
        """
        Test to show that a structure cannot be created with multiple root nodes
        """

        CommonTestCases.admin_token_assert_equal(
            self,
            structure_mutation_multiple_root_nodes,
            structure_mutation_multiple_root_nodes_response
        )

    def test_create_structure_node_appear_before_parent(self):
        """
        Test to show that a structure cannot be created if a node appears
        before its parent in the node list
        """

        CommonTestCases.admin_token_assert_equal(
            self,
            structure_mutation_node_before_parent,
            structure_mutation_node_before_parent_response
        )
