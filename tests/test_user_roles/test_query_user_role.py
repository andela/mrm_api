from tests.base import (
    BaseTestCase,
    CommonTestCases,
    change_user_role_helper,
    change_test_user_role
)
from fixtures.user_role.user_role_fixtures import (
    change_user_role_mutation_query,
    change_unavailable_user_role_mutation_query,
    change_unavailable_user_role_mutation_response,
    user_role_query, user_role_query_response,
    change_user_role_mutation_response,
    query_users_by_user_role,
    query_users_by_user_role_response,
    assign_invalid_user_role_mutation,
    assign_invalid_user_role_response)
from helpers.database import db_session
from api.user.models import User
from api.role.models import Role
import sys
import os
sys.path.append(os.getcwd())
user_role = Role(role="Default")


def create_user():
    user = User(email='mrm@andela.com', location="Kampala",
                name="test test",
                picture="www.andela.com/testuser")
    user.save()
    role = Role.query.filter_by(role='Admin').first()
    user.roles.append(role)
    db_session().commit()
    return user


class TestQueryUserRole(BaseTestCase):
    def test_query_users_role(self):
        """
        Testing for query User role
        """
        user = User(email="info@andela.com", location="Lagos",
                    name="test test",
                    picture="www.andela.com/testuser")
        user.save()

        user.roles.append(user_role)
        db_session().commit()

        execute_query = self.client.execute(
            user_role_query,
            context_value={'session': db_session})
        expected_responese = user_role_query_response
        self.assertEqual(execute_query, expected_responese)

    def test_query_users_role_by_role(self):
        CommonTestCases.admin_token_assert_equal(
            self,
            query_users_by_user_role,
            query_users_by_user_role_response
        )

    @change_test_user_role
    def test_change_user_role(self):
        CommonTestCases.admin_token_assert_in(
            self,
            change_user_role_mutation_query,
            change_user_role_mutation_response
        )

    @change_user_role_helper
    def test_change_unavailable_user_role(self):
        CommonTestCases.admin_token_assert_equal(
            self,
            change_unavailable_user_role_mutation_query,
            change_unavailable_user_role_mutation_response
        )

    @change_user_role_helper
    def test_change_user_role_by_default_user(self):
        CommonTestCases.admin_token_assert_in(
            self,
            change_user_role_mutation_query,
            "You are not authorized to perform this action"
        )

    def test_assign_invalid_role(self):
        create_user()
        CommonTestCases.admin_token_assert_equal(
            self,
            assign_invalid_user_role_mutation,
            assign_invalid_user_role_response
        )
