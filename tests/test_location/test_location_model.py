from tests.base import BaseTestCase
from api.location.models import Location


class TestLocationModel(BaseTestCase):
    def test_if_data_is_saved(self):
        """
        Test if on creation of a location, data is actually saved
        """

        object_count = Location.query.count()

        test_location = Location(name='Kenya',
                                 abbreviation='KY')
        test_location.save()

        new_count = Location.query.count()

        self.assertNotEquals(object_count, new_count)
        assert object_count < new_count
