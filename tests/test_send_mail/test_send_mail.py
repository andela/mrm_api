from unittest.mock import patch

from tests.base import BaseTestCase
from fixtures.email.email_fixtures import create_office_message


class TestCeleryTasks(BaseTestCase):
    def test_send_mail(self):
        with patch('helpers.email.email_setup.SendEmail.send_async_email.delay'
                   ) as send_mail:
            send_mail(create_office_message)
            self.assertTrue(send_mail.called)
