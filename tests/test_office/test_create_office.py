import sys
import os
import json

from tests.base import BaseTestCase
from fixtures.token.token_fixture import admin_api_token
from fixtures.office.office_fixtures import (office_mutation_query, office_mutation_response, office_mutation_query_Different_Location,  # noqa : E501
office_mutation_query_non_existant_ID)

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

    def test_create_office_different_location(self):
        """
        Test creating office in different location
        """
        api_header = {'token': admin_api_token}
        response = self.app_test.post(
            '/mrm?query='+office_mutation_query_Different_Location,
            headers=api_header)
        self.assertIn("You are not authorized to make changes in", str(response.data))  # noqa : E501

    def test_office_creation_with_non_existant_ID(self):
        """
        Testing for office creation with non existant ID
        """

        api_header = {'token': admin_api_token}
        response = self.app_test.post(
            '/mrm?query='+office_mutation_query_non_existant_ID, headers=api_header)  # noqa : E501 
        self.assertIn("Location not found", str(response.data))
