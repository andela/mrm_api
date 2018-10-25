from tests.base import BaseTestCase, CommonTestCases
from fixtures.user.user_fixture import (
    send_invitation_to_existent_user_query,
    send_invitation_to_existent_user_response)


class InviteUser(BaseTestCase):
    def test_admin_invite_to_existent_user(self):
        CommonTestCases.admin_token_assert_equal(
            self, send_invitation_to_existent_user_query,
            send_invitation_to_existent_user_response)
