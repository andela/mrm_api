import sys
import os
sys.path.append(os.getcwd())

from tests.base import BaseTestCase
from api.room.models import Room


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
