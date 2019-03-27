from tests.base import BaseTestCase
from fixtures.structure.structures_fixtures import (
    query_structures,
    expected_response_structures
)

import sys
import os
sys.path.append(os.getcwd())


class TestAllStructures(BaseTestCase):
    def test_all_devices(self):
        query = self.client.execute(query_structures)
        self.assertEquals(query, expected_response_structures)
