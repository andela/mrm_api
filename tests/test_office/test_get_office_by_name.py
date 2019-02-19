import sys
import os

from tests.base import BaseTestCase, CommonTestCases
from fixtures.office.office_fixtures import (
    get_office_by_name,
    get_office_by_name_response,
    get_office_by_wrong_name,
    get_office_by_name_epic_tower)

sys.path.append(os.getcwd())


class GetOfficeByName(BaseTestCase):
    def test_get_office_by_name(self):
        CommonTestCases.user_token_assert_equal(
            self,
            get_office_by_name,
            get_office_by_name_response
        )

    def test_get_office_with_wrong_office(self):
        CommonTestCases.user_token_assert_in(
            self,
            get_office_by_wrong_name,
            "Office Not found"
        )

    def test_get_office_by_name_epic_tower(self):
        CommonTestCases.user_token_assert_in(
            self,
            get_office_by_name_epic_tower,
            "Epic tower"
        )
