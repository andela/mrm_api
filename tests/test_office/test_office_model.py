from tests.base import BaseTestCase
from api.office.models import Office

import sys
import os
sys.path.append(os.getcwd())


class TestOfficesModel(BaseTestCase):
    def test_if_data_can_be_saved(self):
        """
        Test that data can be saved in the Office Model by
        counting number of objects
        """
        object_count = Office.query.count()

        office = Office(name='Wakanda', location_id=1)
        office.save()

        new_count = Office.query.count()

        self.assertNotEquals(object_count, new_count)
        assert object_count < new_count
