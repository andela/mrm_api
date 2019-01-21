from tests.base import BaseTestCase, CommonTestCases

from fixtures.location.update_location_fixtures import (
    query_update_all_fields, query_location_id_non_existant,
    expected_query_update_all_fields, expected_location_id_non_existant_query)


class TestUpdateLocation(BaseTestCase):

    def test_if_all_fields_updated(self):
        CommonTestCases.admin_token_assert_equal(
            self, query_update_all_fields, expected_query_update_all_fields)

    def test_updatelocation_mutation_when_id_is_wrong(self):
        CommonTestCases.admin_token_assert_equal(
            self,
            query_location_id_non_existant,
            expected_location_id_non_existant_query
        )
