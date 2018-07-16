from tests.base import BaseTestCase
from fixtures.office.office_fixtures import (
    rooms_in_office_query,
    rooms_in_office_query_response
)

import sys
import os
sys.path.append(os.getcwd())


class QueryOffice(BaseTestCase):
    def test_get_rooms_in_office(self):
        query = self.client.execute(rooms_in_office_query)
        self.assertEquals(query, rooms_in_office_query_response)
