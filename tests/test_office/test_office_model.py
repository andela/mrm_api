from tests.base import BaseTestCase
from api.office.models import Office

import sys
import os
sys.path.append(os.getcwd())


class TestOfficeModel(BaseTestCase):

    def test_office_creation_with_building_name_empty(self):
        """
        Test office creation with building_nmae field empty
        """
        with self.assertRaises(AttributeError):
            office = Office(
                building_name="",
                time_zone="WAT",
                location_id=1
            )
            office.save()

    def test_office_creation_with_time_zone_empty(self):
        """
        Test office creation with time_zone field empty
        """
        with self.assertRaises(AttributeError):
            office = Office(
                building_name="EPIC Tower",
                time_zone="",
                location_id=1
            )
            office.save()
