from tests.base import BaseTestCase
from fixtures.structure.structures_fixtures import (
    query_structures,
    expected_response_structures
)

from fixtures.token.token_fixture import ADMIN_TOKEN

import sys
import os
sys.path.append(os.getcwd())


class TestAllStructures(BaseTestCase):
    def test_all_structures(self):
        print(ADMIN_TOKEN, '-----------------------------------')
        headers = {"Authorization": "Bearer" + " " + ADMIN_TOKEN}
        query = self.client.execute(query_structures, headers=headers)
        self.assertEquals(query, expected_response_structures)
