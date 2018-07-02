from tests.base import BaseTestCase
from api.devices.models import Devices

import sys
import os
sys.path.append(os.getcwd())


class TestDevicesModel(BaseTestCase):

    def test_device_creation_with_name_empty(self):
        """
        Test room creation with name field empty
        """
        with self.assertRaises(AttributeError):
            device = Devices(
                name="",
                device_type="Internal Display",
                date_added="2018-06-08T11:17:58.785136",
                last_seen="2018-06-08T11:17:58.785136",
                location="Kenya",
                resource_id=1
            )
            device.save()

    def test_device_creation_with_tpe_empty(self):
        """
        Test room creation with device type field empty
        """
        with self.assertRaises(AttributeError):
            device = Devices(
                name="Samsung tablet",
                device_type="",
                date_added="2018-06-08T11:17:58.785136",
                last_seen="2018-06-08T11:17:58.785136",
                location="Kenya",
                resource_id=1
            )
            device.save()

    def test_if_data_can_be_saved(self):
        """
        Test that data can be saved in the Device Model by
        counting number of objects
        """
        object_count = Devices.query.count()

        device = Devices(
                resource_id=1,
                last_seen="2018-06-08T11:17:58.785136",
                date_added="2018-06-08T11:17:58.785136",
                name="Samsung ",
                location="Nairobi",
                device_type="External Display"
            )
        device.save()

        new_count = Devices.query.count()

        self.assertNotEquals(object_count, new_count)
        assert object_count < new_count
