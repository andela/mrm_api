import sys
import os
import json

from tests.base import BaseTestCase
from fixtures.token.token_fixture import admin_api_token
from fixtures.office.office_fixtures import (
    office_mutation_query, office_mutation_response)

sys.path.append(os.getcwd())


class TestCreateOffice(BaseTestCase):

    def test_office_creation(self):
        """
        Testing for office creation
        """

        api_header = {'token': admin_api_token}
        response = self.app_test.post(
            '/mrm?query='+office_mutation_query, headers=api_header)
        expected_response = office_mutation_response
        actual_response = json.loads(response.data)
        self.assertEqual(expected_response, actual_response)
