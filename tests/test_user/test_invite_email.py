from tests.base import BaseTestCase, CommonTestCases
from fixtures.user.user_fixture import (
    send_invitation_to_existent_user_query,
    send_invitation_to_existent_user_response,
    send_invitation_to_nonexistent_user_query)


class InviteUser(BaseTestCase):
    def test_admin_invite_to_existent_user(self):
        CommonTestCases.admin_token_assert_equal(
            self, send_invitation_to_existent_user_query,
            send_invitation_to_existent_user_response)

    def test_admin_invite_to_non_existent_user(self):
        CommonTestCases.admin_token_assert_in(
            self, send_invitation_to_nonexistent_user_query,
            "beverly.kololi@andela.com")
