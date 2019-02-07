from tests.base import BaseTestCase, CommonTestCases
from fixtures.user.user_fixture import (
    user_query, user_query_response,
    query_user_by_email, query_user_email_response,
    paginated_users_query, paginated_users_response,
    get_users_by_location, get_users_by_location_and_role,
    get_user_by_role_reponse, get_users_by_role,
    filter_user_by_location
)
from helpers.database import db_session
from api.user.models import User

import sys
import os
sys.path.append(os.getcwd())


class TestQueryUser(BaseTestCase):

    def test_query_users(self):
        """
        Testing for User creation
        """
        user = User(email='mrm@andela.com',
                    name="test test",
                    picture="www.andela.com/test")
        user.save()

        execute_query = self.client.execute(
            user_query,
            context_value={'session': db_session})

        expected_response = user_query_response
        self.assertEqual(execute_query, expected_response)

    def test_paginate__users_query(self):
        user = User(email='mrm@andela.com',
                    name="test test",
                    picture="www.andela.com/test")
        user.save()

        self.client.execute(
            user_query, context_value={'session': db_session})

        CommonTestCases.admin_token_assert_equal(
            self,
            paginated_users_query,
            paginated_users_response
        )

    def test_query_users_by_email(self):
        user = User(email='mrm@andela.com',
                    name="test test",
                    picture="www.andela.com/test")
        user.save()
        db_session().commit()

        execute_query = self.client.execute(
            query_user_by_email,
            context_value={'session': db_session})

        expected_responese = query_user_email_response
        self.assertEqual(execute_query, expected_responese)

    def test_get_users_by_location_error(self):
        """
        Testing that returns error for no users in location
        """
        CommonTestCases.admin_token_assert_in(
            self, get_users_by_location, "No users found"
        )

    def test_get_user_by_role(self):
        """
        Testing that users can be filtered by role
        """
        CommonTestCases.admin_token_assert_equal(
            self, get_users_by_role, get_user_by_role_reponse
            )

    def test_get_users_by_location_and_role(self):
        """
        Test for error returned for incorrect role id
        """
        CommonTestCases.user_token_assert_in(
            self, get_users_by_location_and_role, "No users found"
            )

    def test_query_users_by_location(self):
        """
        Test for query users with invalid location id
        """
        CommonTestCases.user_token_assert_in(
            self,
            filter_user_by_location,
            "Location id does not exist"
        )
