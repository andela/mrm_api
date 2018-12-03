from tests.base import BaseTestCase, CommonTestCases

from fixtures.floor.update_floor_fixtures import (
    update_floor_mutation,
    update_with_empty_field,
    update_with_nonexistent_floor_id,
    floor_mutation_duplicate_name,
    floor_mutation_duplicate_name_response
)


class TestUpdateFloor(BaseTestCase):
    def test_if_all_fields_updates(self):
        CommonTestCases.admin_token_assert_in(
            self,
            update_floor_mutation,
            "2nd"
        )

    def test_floor_update_with_name_empty(self):
        CommonTestCases.admin_token_assert_in(
            self,
            update_with_empty_field,
            "name is required field"
        )

    def test_floor_update_with_duplicate_name(self):
        CommonTestCases.admin_token_assert_equal(
            self,
            floor_mutation_duplicate_name,
            floor_mutation_duplicate_name_response
        )

    def test_for_error_if_floor_id_is_non_existant_room(self):
        CommonTestCases.admin_token_assert_in(
            self,
            update_with_nonexistent_floor_id,
            "Floor not found")
