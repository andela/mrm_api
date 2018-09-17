import json

from tests.base import BaseTestCase
from fixtures.office.office_fixtures import (
    paginated_offices_query,
    offices_query_response,
    offices_query,
    all_offices_query_response,
    paginated_offices_non_existing_page_query
    )


class QueryOffice(BaseTestCase):

    def test_paginate_office_query(self):
        response = self.app_test.post('/mrm?query='+paginated_offices_query)
        paginate_query = json.loads(response.data)
        expected_response = offices_query_response
        self.assertEqual(paginate_query, expected_response)

    def test_office_query(self):
        response = self.app_test.post('/mrm?query='+offices_query)
        paginate_query = json.loads(response.data)
        expected_response = all_offices_query_response
        self.assertEqual(paginate_query, expected_response)

    def test_office_non_existing_page_paginated_query(self):
        response = self.app_test.post('/mrm?query='+paginated_offices_non_existing_page_query)  # noqa: E501
        self.assertIn("No more offices", str(response.data))
