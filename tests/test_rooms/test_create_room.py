from tests.base import BaseTestCase
from fixtures.token.token_fixture import admin_api_token
from fixtures.helpers.decorators_fixtures import (
    query_string, query_string_response
    )

import sys
import os
sys.path.append(os.getcwd())


class TestCreateRoom(BaseTestCase):

    def test_room_creation(self):
        """
        Testing for room creation
        """

        api_headers = {'token': admin_api_token}
        query = self.app_test.post(query_string, headers=api_headers)
        expected_response = query_string_response

        self.assertEqual(query.data, expected_response)
