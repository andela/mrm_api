import json

from tests.base import BaseTestCase

from fixtures.office.office_fixtures import (delete_office_mutation,
delete_non_existent_office_mutation,
delete_unauthorised_location_mutation)  # noqa: E501
from fixtures.token.token_fixture import admin_api_token


class TestDeleteOffice(BaseTestCase):
    def test_delete_office(self):
        headers = {"Authorization": "Bearer" + " " + admin_api_token}
        response = self.app_test.post('/mrm?query='+delete_office_mutation,
                                      headers=headers)
        self.assertIn("St. Catherines", str(response.data))

    def test_delete_non_existent_office(self):
        headers = {"Authorization": "Bearer" + " " + admin_api_token}
        response = self.app_test.post('/mrm?query='+delete_non_existent_office_mutation,  # noqa: E501
                                      headers=headers)
        self.assertIn("Office not found", str(response.data))

    def test_delete_unautorised_location(self):
        headers = {"Authorization": "Bearer" + " " + admin_api_token}
        response = self.app_test.post('mrm?query='+delete_unauthorised_location_mutation,  # noqa: E501
                                      headers=headers)
        expected_response = json.loads(response.data)
        self.assertIn("You are not authorized to make changes in Nairobi", expected_response['errors'][0]['message'])  # noqa: E501
