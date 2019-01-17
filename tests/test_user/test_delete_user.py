import sys
import os

from tests.base import BaseTestCase, CommonTestCases
from fixtures.user.delete_user import (
    delete_user, expected_query_after_delete, delete_self, user_not_found,
    delete_user_2, user_invalid_email)
from api.user.models import User
from api.role.models import Role
import tests.base as base


sys.path.append(os.getcwd())


class TestDeleteUser(BaseTestCase):
    def test_deleteuser_when_not_admin(self):
        CommonTestCases.user_token_assert_in(
            self,
            delete_user,
            "You are not authorized to perform this action"
        )

    def test_deleteuser_when_admin(self):
        user = User(email="test.test@andela.com",
                    location="Kampala", name="test test",
                    picture="www.andela.com/test")
        user.save()
        role = Role(role="Default User")
        role.save()
        user.roles.append(role)

        CommonTestCases.admin_token_assert_equal(
            self,
            delete_user_2,
            expected_query_after_delete
        )

    def test_user_delete_admin(self):
        admin_user = User(email="new.user@andela.com",
                          location="Kampala", name="test test",
                          picture="www.andela.com/test")
        admin_user.save()
        role = base.role
        admin_user.roles.append(role)

        CommonTestCases.user_token_assert_in(
            self,
            delete_user,
            "You are not authorized to perform this action"
        )

    def test_delete_self(self):
        CommonTestCases.admin_token_assert_in(
            self,
            delete_self,
            "You cannot delete yourself"
        )

    def test_deleteuser_not_found(self):
        CommonTestCases.admin_token_assert_in(
            self,
            user_not_found,
            "User not found"
        )

    def test_deleteuser_invalid_email(self):
        CommonTestCases.admin_token_assert_in(
            self,
            user_invalid_email,
            "Invalid email format"
        )
