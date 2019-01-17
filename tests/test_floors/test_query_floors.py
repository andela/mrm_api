from tests.base import BaseTestCase

from fixtures.floor.get_floors_fixures import (
    get_all_floors_query,
    get_floors_query_response,
    paginated_floors_query,
    paginated_floors_response
)

import sys
import os
sys.path.append(os.getcwd())


class TestQueryFloors(BaseTestCase):
    def test_query_all_floors(self):
        all_floors = self.client.execute(get_all_floors_query)
        self.assertEquals(all_floors, get_floors_query_response)

    def test_query_paginated_floors(self):
        paginated_floors = self.client.execute(paginated_floors_query)
        self.assertEquals(paginated_floors, paginated_floors_response)
