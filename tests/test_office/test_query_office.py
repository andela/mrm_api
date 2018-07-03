from tests.base import BaseTestCase

from fixtures.office.office_fixtures import (
    get_all_offices_query, get_offices_query_response
)

import sys
import os
sys.path.append(os.getcwd())


class TestQueryOffices(BaseTestCase):
    def test_query_all_offices(self):
        all_offices = self.client.execute(get_all_offices_query)
        self.assertEquals(all_offices, get_offices_query_response)
