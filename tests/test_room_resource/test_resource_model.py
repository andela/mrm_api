from tests.base import BaseTestCase
from api.room_resource.models import Resource


class TestBlockModel(BaseTestCase):
    def test_if_data_can_be_saved(self):
        """
        Test that data can be saved in the Block Model by
        counting number of objects
        """
        object_count = Resource.query.count()

        resource = Resource(name="TV Screen", quantity=3)
        resource.save()

        new_count = Resource.query.count()

        self.assertNotEquals(object_count, new_count)
        assert object_count < new_count
