from unittest.mock import patch
from tests.base import BaseTestCase
from helpers.calendar.calendar import get_events_mock_data
from fixtures.events.sync_events_data_fixture import (
    sync_data_mutation,
    sync_data_response,
    notification_response,
    notification_mutation
)


@patch("helpers.calendar.events.get_google_calendar_events",
       spec=True)
class TestSyncEvents(BaseTestCase):
    def test_sync_all_events(self, mocked_method):
        mocked_method.return_value = get_events_mock_data()
        response = self.client.execute(sync_data_mutation)
        self.assertEqual(sync_data_response, response)

    def test_syncs_after_notification_is_recieved(self, mocked_method):
        mocked_method.return_value = get_events_mock_data()
        response = self.client.execute(notification_mutation)
        self.assertEqual(notification_response, response)
