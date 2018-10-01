import json
from tests.base import BaseTestCase
from fixtures.token.token_fixture import admin_api_token
from fixtures.room.room_analytics_daily_duration_fixtures import (
    get_daily_meetings_total_duration_query,
    get_daily_meetings_total_duration_response
)


class TotalDailyDurations(BaseTestCase):

    def test_total_daily_durations(self):
        """
        Tests getting total durations for daily meetings
        """

        headers = {"Authorization": "Bearer" + " " + admin_api_token}
        response = self.app_test.post('/mrm?query='+get_daily_meetings_total_duration_query, headers=headers)  # noqa: E501
        actual_response = json.loads(response.data)
        self.assertEquals(actual_response, get_daily_meetings_total_duration_response)  # noqa: E501
