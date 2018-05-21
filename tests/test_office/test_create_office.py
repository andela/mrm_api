from tests.base import BaseTestCase
from fixtures.office.create_ofice_fixtures import (
    office_mutation_query, office_mutation_response
)
from helpers.database import db_session

import sys
import os
sys.path.append(os.getcwd())


class TestCreateOffice(BaseTestCase):

    def test_office_creation(self):
        """
        Testing for office creation
        """
        execute_query = self.client.execute(
            office_mutation_query,
            context_value={'session': db_session})

        expected_responese = office_mutation_response
        self.assertEqual(execute_query, expected_responese)
