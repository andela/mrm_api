from tests.base import BaseTestCase

from fixtures.office.office_fixtures import (delete_office_mutation,
delete_non_existent_office_mutation,
delete_unauthorised_location_mutation)  # noqa: E501
from fixtures.token.token_fixture import admin_api_token


class TestDeleteOffice(BaseTestCase):
    def test_delete_office(self):
        api_headers = {'token': admin_api_token}
        response = self.app_test.post('/mrm?query='+delete_office_mutation,
                                      headers=api_headers)
        self.assertIn("St. Catherines", str(response.data))

    def test_delete_non_existent_office(self):
        api_headers = {'token': admin_api_token}
        response = self.app_test.post('/mrm?query='+delete_non_existent_office_mutation,  # noqa: E501
                                      headers=api_headers)
        self.assertIn("Office not found", str(response.data))

    def test_delete_unautorised_location(self):
        api_headers = {'token': admin_api_token}
        response = self.app_test.post('mrm?query='+delete_unauthorised_location_mutation,  # noqa: E501
                                      headers=api_headers)
        self.assertIn("You are not authorized to delete an office in Nairobi", str(response.data))  # noqa: E501
