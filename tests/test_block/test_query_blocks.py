from tests.base import BaseTestCase

from fixtures.block.block_fixtures import (
    get_all_blocks_query, get_blocks_query_response
)

import sys
import os
sys.path.append(os.getcwd())


class TestQueryBlocks(BaseTestCase):
    def test_query_all_blocks(self):
        all_blocks = self.client.execute(get_all_blocks_query)
        self.assertEquals(all_blocks, get_blocks_query_response)
