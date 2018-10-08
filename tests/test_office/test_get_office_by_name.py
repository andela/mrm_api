import sys
import os

from tests.base import BaseTestCase, CommonTestCases
from fixtures.office.office_fixtures import (
    get_office_by_name,
    get_office_by_name_response)

sys.path.append(os.getcwd())


class GetOfficeByName(BaseTestCase):
    def test_get_office_by_name(self):
        CommonTestCases.user_token_assert_equal(
            self,
            get_office_by_name,
            get_office_by_name_response
        )
