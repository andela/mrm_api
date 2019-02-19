import json

from tests.base import BaseTestCase
from helpers.database import engine, db_session
from fixtures.office.office_fixtures import (
    paginated_offices_query,
    offices_query,
    )


class QueryOffice(BaseTestCase):
    def test_paginate_office_query(self):
        db_session.remove()
        with engine.begin() as conn:
            conn.execute("DROP TABLE locations CASCADE")
            conn.execute("DROP TABLE offices CASCADE")
        response = self.app_test.post('/mrm?query='+paginated_offices_query)
        paginate_query = json.loads(response.data)
        self.assertIn(
            "There seems to be a database connection error",
            str(paginate_query))

    def test_office_query(self):
        db_session.remove()
        with engine.begin() as conn:
            conn.execute("DROP TABLE locations CASCADE")
            conn.execute("DROP TABLE offices CASCADE")
        response = self.app_test.post('/mrm?query='+offices_query)
        paginate_query = json.loads(response.data)
        self.assertIn(
            "There seems to be a database connection error",
            str(paginate_query))
