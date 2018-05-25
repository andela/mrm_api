from tests.base import BaseTestCase
from fixtures.room.room_fixtures import (
    room_mutation_query, room_mutation_response
)
from helpers.database import db_session
from fixtures.helpers.decorators_fixtures import ( 
    admin_token, query_string, query_string_response
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
        execute_query = self.client.execute(
            room_mutation_query,
            context_value={'session': db_session})

        expected_responese = room_mutation_response
        self.assertEqual(execute_query, expected_responese)
        user = User(email="admin@mrm.com")
        user.save()
        role = Role(role="Admin")
        role.save()
        user_role = UsersRole(user_id=user.id, role_id=role.id)
        user_role.save()
        db_session().commit()

        query = self.app_test.post(query_string, headers={'token': admin_token})

        expected_response = query_string_response

        self.assertEqual(query.data, expected_response)

        # execute_query = self.client.execute(
        #     room_mutation_query,
        #     # headers={'token': admin_token},
        #     context_value={'session': db_session})
        
        # expected_responese = room_mutation_response
        # self.assertEqual(execute_query, expected_responese)
