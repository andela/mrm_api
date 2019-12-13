import unittest
from unittest.mock import patch
from helpers.event.slack_notifier import notify_slack


class TestSlackNotifier(unittest.TestCase):

    @patch('helpers.event.slack_notifier.requests.get')
    def test_slack_notifier(self, mock_get_request):
        """
        Test to verify that a request is made when
        an event ends
        """
        notify_slack('event_id', 'andela@andela.com', '18')
        mock_get_request.assert_called_once()
