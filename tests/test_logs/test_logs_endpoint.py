import os
import sys
from tests.base import BaseTestCase, change_admin_user_role_to_super_admin
from fixtures.token.token_fixture import ADMIN_TOKEN

sys.path.append(os.getcwd())


class TestLogs(BaseTestCase):
    @change_admin_user_role_to_super_admin
    def test_super_admin_can_view_logs(self):
        """
        Test successful display of the backend logs by the super admin
        """
        url = '/logs'
        headers = {"Authorization": "Bearer " + ADMIN_TOKEN}
        response = self.app_test.get(url, headers=headers)
        self.assert200(response)
