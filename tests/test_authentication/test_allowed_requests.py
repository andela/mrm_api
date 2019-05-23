from unittest.mock import patch, Mock
from tests.base import BaseTestCase
from helpers.auth.allowed_requests import validate_origins


class TestAllowedRequests(BaseTestCase):
    @patch("helpers.auth.allowed_requests.request.headers.get",
    Mock(return_value={'User-Agent': ['insomnia', 'postman']}))  # noqa 501
    @patch("helpers.auth.allowed_requests.os.getenv",
           Mock(return_value='production'))
    def test_wrong_user_agent_in_production(self):
        response = validate_origins()
        self.assertIn(
            b'Invalid request. You are not allowed to make requests to this environment',  # noqa 501
            response[0].data)
