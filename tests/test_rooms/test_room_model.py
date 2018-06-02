from tests.base import BaseTestCase
from api.room.models import Room

import sys
import os
sys.path.append(os.getcwd())


class TestRoomModel(BaseTestCase):

    def test_room_creation_with_name_empty(self):
        """
        Test room creation with name field empty
        """
        with self.assertRaises(AttributeError):
            room = Room(
                name="",
                room_type="Meeting",
                capacity=2,
                floor_id=1
            )
            room.save()

    def test_room_creation_with_type_empty(self):
        """
        Test room creation with room type field empty
        """
        with self.assertRaises(AttributeError):
            room = Room(
                name="Mbarara",
                room_type="",
                capacity=2,
                floor_id=1
            )
            room.save()

    def test_if_data_can_be_saved(self):
        """
        Test that data can be saved in the Room Model by
        counting number of objects
        """
        object_count = Room.query.count()

        room = Room(name='Jinja', room_type='meeting', capacity=5, floor_id=1,
                    image_url="https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg")  # noqa: E501
        room.save()

        new_count = Room.query.count()

        self.assertNotEquals(object_count, new_count)
        assert object_count < new_count
