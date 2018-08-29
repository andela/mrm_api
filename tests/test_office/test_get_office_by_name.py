import sys
import os
import json

from tests.base import BaseTestCase
from fixtures.token.token_fixture import user_api_token
from fixtures.office.office_fixtures import (
    get_office_by_name,
    get_office_by_name_response)

sys.path.append(os.getcwd())


class GetOfficeByName(BaseTestCase):
    def test_get_office_by_name(self):
        api_headers = {'token': user_api_token}
        get_office_query = self.app_test.post(
            '/mrm?query='+get_office_by_name, headers=api_headers)
        actual_response = json.loads(get_office_query.data)
        self.assertEquals(actual_response, get_office_by_name_response)
