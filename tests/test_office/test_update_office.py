import sys
import os
import json

from tests.base import BaseTestCase
from fixtures.token.token_fixture import admin_api_token
from fixtures.office.update_office_fixture import (
    update_office_in_another_location_query,
    update_office_with_wrong_ID_query,
    update_office_with_same_Name_query,
    update_office_query,
    office_mutation_response
    )
sys.path.append(os.getcwd())


class TestUpdateOffice(BaseTestCase):

    def test_update_office(self):
        """
        Test updating an existing office
        """
        api_header = {'token': admin_api_token}
        response = self.app_test.post('/mrm?query='+update_office_query, headers=api_header)  # noqa: E501
        expected_response = office_mutation_response
        actual_response = json.loads(response.data)
        self.assertEqual(expected_response, actual_response)

    def test_updating_non_existant_office(self):
        """
        Test updating a non existing office
        """
        api_header = {'token': admin_api_token}
        response = self.app_test.post('/mrm?query='+update_office_with_wrong_ID_query, headers=api_header)  # noqa: E501
        self.assertIn("Office not found", str(response.data))

    def test_updating_office_name_with_an_existing_name(self):
        """
        Test updating office name with an already existing name
        """
        api_header = {'token': admin_api_token}
        response = self.app_test.post('/mrm?query='+update_office_with_same_Name_query, headers=api_header)  # noqa: E501
        self.assertIn("Action Failed", str(response.data))

    def test_updating_office_in_another_location(self):
        """
        Test updating office in another location
        """
        api_header = {'token': admin_api_token}
        response = self.app_test.post('/mrm?query='+update_office_in_another_location_query, headers=api_header)  # noqa: E501
        self.assertIn("You are not authorized to make changes in", str(response.data))  # noqa: E501
