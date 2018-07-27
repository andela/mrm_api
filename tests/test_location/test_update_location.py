

from tests.base import BaseTestCase

from fixtures.location.update_location_fixtures import (
    query_update_all_fields,
    query_location_id_non_existant
)


class TestUpdateLocation(BaseTestCase):

    def test_if_all_fields_updated(self):
        response = self.app_test.post('/mrm?query='+query_update_all_fields)
        self.assertIn("Nairobi", str(response.data))

    def test_updatelocation_mutation_when_id_is_wrong(self):
        response = self.app_test.post(
            '/mrm?query='+query_location_id_non_existant)
        self.assertIn("Location not found", str(response.data))
