from tests.base import BaseTestCase
from fixtures.block.block_fixtures import (
    rooms_in_block_query,
    rooms_in_block_query_response
)

import sys
import os
sys.path.append(os.getcwd())


class QueryBlock(BaseTestCase):
    def test_get_rooms_in_block(self):
        query = self.client.execute(rooms_in_block_query)
        self.assertEquals(query, rooms_in_block_query_response)
