from tests.base import BaseTestCase

from fixtures.wing.wing_fixtures import (
   get_all_wings_query,
   get_all_wings_query_response,
   paginated_wings_query,
   paginated_wings_query_response
)

import sys
import os
sys.path.append(os.getcwd())


class TestQueryWings(BaseTestCase):
    def test_query_all_wings(self):
        all_wings = self.client.execute(get_all_wings_query)
        self.assertEquals(all_wings, get_all_wings_query_response)

    def test_query_paginated_wings(self):
        paginated_wings = self.client.execute(paginated_wings_query)
        self.assertEquals(paginated_wings, paginated_wings_query_response)
