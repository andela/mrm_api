from tests.base import BaseTestCase, CommonTestCases

from fixtures.floor.delete_floor_fixtures import (
    delete_floor_mutation,
    delete_with_nonexistent_floor_id,
)


class TestDeleteRoom(BaseTestCase):
    def test_delete_floor_admin_user(self):
        CommonTestCases.admin_token_assert_in(
            self,
            delete_floor_mutation,
            "3rd"
        )

    def test_delete_floor_non_admin_user(self):
        CommonTestCases.user_token_assert_in(
            self,
            delete_floor_mutation,
            "You are not authorized to perform this action"
        )

    def test_non_existant_floor_id(self):
        CommonTestCases.admin_token_assert_in(
            self,
            delete_with_nonexistent_floor_id,
            "Floor not found"
        )
