from tests.base import BaseTestCase, change_user_role_helper
from fixtures.user_role.user_role_fixtures import (
    user_role_query, user_role_query_response,
    query_user_by_user_id, query_user_by_user_id_response, change_user_role_mutation_query, change_unavailable_user_role_mutation_query, change_unavailable_user_role_mutation_response,  # noqa E501
    change_user_role_mutation_response
)
from helpers.database import db_session
from api.user.models import User
from api.user_role.models import UsersRole
from fixtures.token.token_fixture import admin_api_token

import sys
import os
import json
sys.path.append(os.getcwd())


class TestQueryUserRole(BaseTestCase):

    def test_query_users_role(self):
        """
        Testing for query User role
        """
        user = User(email="info@andela.com", location="Lagos",
                    name="test test",
                    picture="www.andela.com/testuser")
        user.save()
        user_role = UsersRole(user_id=user.id, role_id=1)
        user_role.save()
        db_session().commit()

        execute_query = self.client.execute(
            user_role_query,
            context_value={'session': db_session})

        expected_responese = user_role_query_response
        self.assertEqual(execute_query, expected_responese)

    def test_query_users_role_by_role(self):
        user = User(email='mrm@andela.com', location="Lagos",
                    name="test test",
                    picture="www.andela.com/testuser")
        user.save()
        user_role = UsersRole(user_id=user.id, role_id=1)
        user_role.save()
        db_session().commit()

        execute_query = self.client.execute(
            query_user_by_user_id,
            context_value={'session': db_session})

        expected_response = query_user_by_user_id_response
        self.assertEqual(execute_query, expected_response)

    def test_change_user_role(self):
        api_headers = {'token': admin_api_token}
        user = User(email='mrm@andela.com', location="Kampala",
                    name="test test",
                    picture="www.andela.com/testuser")
        user.save()
        user_role = UsersRole(user_id=user.id, role_id=1)
        user_role.save()
        db_session().commit()

        query_response = self.app_test.post(
            '/mrm?query='+change_user_role_mutation_query, headers=api_headers)
        actual_response = json.loads(query_response.data)

        expected_response = change_user_role_mutation_response
        self.assertEqual(actual_response, expected_response)

    @change_user_role_helper
    def test_change_unavailable_user_role(self, api_headers):

        query_response = self.app_test.post(
            '/mrm?query='+change_unavailable_user_role_mutation_query,
            headers=api_headers)
        actual_response = json.loads(query_response.data)

        expected_response = change_unavailable_user_role_mutation_response
        self.assertEqual(actual_response, expected_response)

    @change_user_role_helper
    def test_change_user_role_by_default_user(self, api_headers):

        query_response = self.app_test.post(
            '/mrm?query='+change_user_role_mutation_query, headers=api_headers)
        actual_response = json.loads(query_response.data)

        expected_response = "You are not authorized to perform this action"
        self.assertEqual(actual_response["errors"][0]["message"],
                         expected_response)
