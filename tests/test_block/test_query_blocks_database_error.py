from tests.base import BaseTestCase

from helpers.database import engine, db_session
from fixtures.block.block_fixtures import (
    get_all_blocks_query,
    rooms_in_block_query
)

import sys
import os
sys.path.append(os.getcwd())


class TestQueryBlocks(BaseTestCase):
    def test_query_all_blocks(self):
        db_session.remove()
        with engine.begin() as conn:
            conn.execute("DROP TABLE locations CASCADE")
            conn.execute("DROP TABLE blocks CASCADE")
        all_blocks = self.client.execute(get_all_blocks_query)
        self.assertIn(
            "There seems to be a database connection error", str(all_blocks))

    def test_get_rooms_in_block(self):
        db_session.remove()
        with engine.begin() as conn:
            conn.execute("DROP TABLE locations CASCADE")
            conn.execute("DROP TABLE blocks CASCADE")
        query = self.client.execute(rooms_in_block_query)
        self.assertIn(
            "relation \"blocks\" does not exist", str(query))
