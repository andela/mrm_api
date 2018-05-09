from tests.base import BaseTestCase
from api.floor.models import Floor



class TestBlockModel(BaseTestCase):
    def test_if_data_can_be_saved(self):
        """
        Test that data can be saved in the Block Model by
        counting number of objects
        """
        object_count = Floor.query.count()

        floor = Floor(name='2nd', block_id=1)
        floor.save()

        new_count = Floor.query.count()

        self.assertNotEquals(object_count,new_count)
        assert object_count < new_count
