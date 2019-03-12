from tests.base import BaseTestCase, CommonTestCases
from fixtures.office_structure.create_node_fixtures import (
    node_creation_mutation,
    duplicate_node_creation,
    child_node_creation_mutation_with_non_existent_parent_id,
    node_creation_mutation_with_non_existent_tag_id
)
from api.office_structure.models import OfficeStructure


class TestAddNode(BaseTestCase):

    def test_add_node(self):
        """
        Tests an admin can add a node
        """

        CommonTestCases.admin_token_assert_in(
            self,
            node_creation_mutation,
            "floors"
        )

    def test_add_duplicate_node(self):
        """
        Tests an admin can not create two nodes
        with the same name
        """
        CommonTestCases.admin_token_assert_in(
            self,
            duplicate_node_creation,
            "location node level already exists"
        )

    def test_add_child_node_with_non_existent_parent_id(self):
        """
        Tests an admin can not create
        a child node with a non_existent
        parentId
        """
        CommonTestCases.admin_token_assert_in(
            self,
            child_node_creation_mutation_with_non_existent_parent_id,
            "Parent node ID Provided does not exist"
        )

    def test_add_node_with_non_existent_tag_id(self):
        """
        Tests an admin can not create
        a node with a non_existent
        tagId
        """
        CommonTestCases.admin_token_assert_in(
            self,
            node_creation_mutation_with_non_existent_tag_id,
            "Tag ID Provided does not exist"
        )

    def test_add_node_method(self):
        """
        Tests a node can be
        created using the add node
        method in the office structure model
        """
        structure = OfficeStructure()
        structure.add_node(name="root")
        # Add root node
        root_node = OfficeStructure.query.filter_by(id=1).first()
        self.assertEqual(root_node.parent_id, None)
        # Add child node
        structure.add_node(name="floor", parent_id=1)
        child_node = OfficeStructure.query.filter_by(id=2).first()
        self.assertEqual(child_node.parent_id, 1)
        nodes = OfficeStructure.query.all()
        self.assertEqual(len(nodes), 4)
        node_tags = OfficeStructure.query.filter_by(id=1).first()
        self.assertEqual(node_tags.tag_id, 1)

    def test_add_branch(self):
        """
        Tests a branch can be
        created using the add branch method
        in the office structure model
        """
        # create root node
        structure = OfficeStructure()
        structure.add_node(name="root")
        # create list of nodes for branch
        nodes = []
        node_1 = OfficeStructure(name="floor", parent_id=1)
        nodes.append(node_1)
        node_2 = OfficeStructure(name="room", parent_id=2)
        nodes.append(node_2)
        structure.add_branch(nodes)
        nodes_list = OfficeStructure.query.all()
        self.assertEqual(len(nodes_list), 5)
