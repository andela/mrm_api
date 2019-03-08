import json
from tests.base import BaseTestCase
from fixtures.office_structure.get_node_fixtures import (
    get_node_query,
    get_node_query_response,
    get_node_non_existant_id_query,
    get_node_with_non_existant_id_response
)


class TestQueryNode(BaseTestCase):
    def test_get_node_query(self):
        """
        Test can get specific node by id
        """
        response = self.client.execute(get_node_query)
        actual_response = json.loads(json.dumps(response))
        self.assertEquals(actual_response, get_node_query_response)

    def test_get_node_with_non_existant_id(self):
        """
        Test cannot get node with non-existant id
        """
        actual_response = self.client.execute(get_node_non_existant_id_query)
        expected_response = get_node_with_non_existant_id_response
        self.assertEquals(
            actual_response["errors"][0]['message'], expected_response
        )
