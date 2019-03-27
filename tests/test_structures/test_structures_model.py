from tests.base import BaseTestCase
from api.structure.models import Structure

import sys
import os
sys.path.append(os.getcwd())


class TestStructureModel(BaseTestCase):

    def test_if_data_can_be_saved(self):
        """
        Test that data can be saved in the Structure Model by
        counting number of objects
        """
        object_count = Structure.query.count()

        structure = Structure(
                web_id="azxtuvwertyuo",
                level=3,
                name="Epic Tower",
                location_id=1,
                position=1,
                parent_id=3,
                tag="Ilupeju"
            )
        structure.save()

        new_count = Structure.query.count()

        self.assertNotEquals(object_count, new_count)
        assert object_count < new_count
