import json

from tests.base import BaseTestCase, CommonTestCases
from fixtures.office.update_delete_office_fixture import (
    delete_office_mutation,
    delete_office_mutation_response,
    delete_non_existent_office_mutation,
    delete_unauthorised_location_mutation
)
from fixtures.token.token_fixture import ADMIN_TOKEN


class TestDeleteOffice(BaseTestCase):
    def test_delete_office(self):
        CommonTestCases.admin_token_assert_equal(
            self,
            delete_office_mutation,
            delete_office_mutation_response
        )

    def test_delete_non_existent_office(self):
        CommonTestCases.admin_token_assert_in(
            self,
            delete_non_existent_office_mutation,
            "Office not found"
        )

    def test_delete_unautorised_location(self):
        headers = {"Authorization": "Bearer" + " " + ADMIN_TOKEN}
        response = self.app_test.post('mrm?query='+delete_unauthorised_location_mutation,  # noqa: E501
                                      headers=headers)
        expected_response = json.loads(response.data)
        self.assertIn("You are not authorized to make changes in Nairobi", expected_response['errors'][0]['message'])  # noqa: E501
