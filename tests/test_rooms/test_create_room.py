from tests.base import BaseTestCase
from helpers.database import db_session
from fixtures.token.token_fixture import api_token
from fixtures.helpers.decorators_fixtures import (
    query_string, query_string_response
    )

from api.user.models import User
from api.role.models import Role
from api.user_role.models import UsersRole

import sys
import os
sys.path.append(os.getcwd())


class TestCreateRoom(BaseTestCase):

    def test_room_creation(self):
        """
        Testing for room creation
        """

        user = User(email="patrick.walukagga@andela.com", location="Lagos")
        user.save()
        role = Role(role="Admin")
        role.save()
        user_role = UsersRole(user_id=user.id, role_id=role.id)
        user_role.save()
        db_session().commit()

        api_headers = {'token': api_token}
        query = self.app_test.post(query_string, headers=api_headers)
        expected_response = query_string_response

        self.assertEqual(query.data, expected_response)
