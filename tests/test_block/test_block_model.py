from tests.base import BaseTestCase
from api.block.models import Block

import sys
import os
sys.path.append(os.getcwd())


class TestBlocksModel(BaseTestCase):
    def test_if_data_can_be_saved(self):
        """
        Test that data can be saved in the Block Model by
        counting number of objects
        """
        object_count = Block.query.count()

        block = Block(name='Wakanda', office_id=1)
        block.save()

        new_count = Block.query.count()

        self.assertNotEquals(object_count, new_count)
        assert object_count < new_count
