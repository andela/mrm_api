from tests.base import BaseTestCase
from fixtures.devices.devices_fixtures import (
    update_device_query,
    expected_update_device_response,
    query_with_non_existant_id,
    non_existant_id_response

)


class TestUpdateDevices(BaseTestCase):
    def test_update_device(self):
        query = self.client.execute(update_device_query)
        self.assertEquals(query, expected_update_device_response)

    def test_update_device_with_non_existant_id(self):
        query = self.client.execute(query_with_non_existant_id)
        self.assertEquals(query, non_existant_id_response)
