from tests.base import BaseTestCase, CommonTestCases
from fixtures.location.delete_location_fixtures import (
    delete_location_query,
    delete_location_response,
    delete_non_existent_location,
)


class TestDeleteLocation(BaseTestCase):
    def test_delete_location(self):
        CommonTestCases.admin_token_assert_equal(
            self,
            delete_location_query,
            delete_location_response
        )

    def test_delete_non_existent_location(self):
        CommonTestCases.admin_token_assert_in(
            self,
            delete_non_existent_location,
            "location not found"
        )
