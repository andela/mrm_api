import sys
import os
sys.path.append(os.getcwd())
from os.path import dirname, abspath
mrm_api = dirname(dirname(abspath(__file__)))
sys.path.insert(0, mrm_api)

from tests.base import BaseTestCase
from fixtures.block.block_fixtures import(
    rooms_in_block_query,
    rooms_in_block_query_response
)


class QueryBlock(BaseTestCase):
    def test_get_rooms_in_block(self):
        query = self.client.execute(rooms_in_block_query)
        assert query == rooms_in_block_query_response
