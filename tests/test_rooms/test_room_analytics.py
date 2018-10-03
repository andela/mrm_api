import json

from tests.base import BaseTestCase
from fixtures.token.token_fixture import (admin_api_token)
from fixtures.room.room_analytics_fixtures import (
    get_most_used_room_in_a_month_analytics_query,
    get_most_used_room_in_a_month_analytics_response,
    most_used_room_in_a_month_analytics_invalid_location_query,
    most_used_room_in_a_month_analytics_invalid_location_response,
    get_least_used_room_per_week_query,
    get_least_used_room_per_week_response,
    get_least_used_room_without_event_query,
    get_least_used_room_without_event_response,
    most_used_room_per_day_query,
    most_used_room_per_day_response
    get_room_usage_analytics,
    get_room_usage_anaytics_respone,
    get_room_usage_analytics_invalid_location,
    get_room_usage_analytics_invalid_location_response,

)


class QueryRoomsAnalytics(BaseTestCase):


    def test_most_used_room_in_a_month_analytics(self):
        headers = {"Authorization": "Bearer" + " " + admin_api_token}
        response = self.app_test.post(
            '/mrm?query=' + get_most_used_room_in_a_month_analytics_query, headers=headers)  # noqa: E501
        actual_response = json.loads(response.data)
        expected_response = get_most_used_room_in_a_month_analytics_response
        self.assertEquals(actual_response, expected_response)

    def test_most_used_room_in_a_month_invalid_location_analytics(self):
        headers = {"Authorization": "Bearer" + " " + admin_api_token}
        response = self.app_test.post(
            '/mrm?query=' + most_used_room_in_a_month_analytics_invalid_location_query, headers=headers)  # noqa: E501
        actual_response = json.loads(response.data)
        expected_response = most_used_room_in_a_month_analytics_invalid_location_response  # noqa: E501
        self.assertEquals(actual_response, expected_response)

    def test_analytics_for_least_used_room_weekly(self):
        headers = {"Authorization": "Bearer" + " " + admin_api_token}
        analytics_query = self.app_test.post(
            '/mrm?query=' + get_least_used_room_per_week_query, headers=headers)  # noqa: E501
        actual_response = json.loads(analytics_query.data)
        expected_response = get_least_used_room_per_week_response
        self.assertEquals(actual_response, expected_response)

    def test_analytics_for_least_used_room_without_event_weekly(self):
        headers = {"Authorization": "Bearer" + " " + admin_api_token}
        analytics_query = self.app_test.post(
            '/mrm?query=' + get_least_used_room_without_event_query, headers=headers)  # noqa: E501
        actual_response = json.loads(analytics_query.data)
        expected_response = get_least_used_room_without_event_response
        self.assertEquals(actual_response, expected_response)

    def test_analytics_for_most_used_room_per_day(self):
        headers = {"Authorization": "Bearer" + " " + admin_api_token}
        analytics_query = self.app_test.post(
            '/mrm?query=' + most_used_room_per_day_query, headers=headers)  # noqa: E501
        actual_response = json.loads(analytics_query.data)
        expected_response = most_used_room_per_day_response
    def test_room_usage_analytics(self):
        headers = {"Authorization": "Bearer" + " " + admin_api_token}
        response = self.app_test.post(
            '/mrm?query='+get_room_usage_analytics, headers=headers)
        actual_response = json.loads(response.data)
        expected_response = get_room_usage_anaytics_respone
        self.assertEquals(actual_response, expected_response)

    def test_room_usage_analytics_invalid_location(self):
        headers = {"Authorization": "Bearer" + " " + admin_api_token}
        response = self.app_test.post(
            '/mrm?query='+get_room_usage_analytics_invalid_location,
            headers=headers)
        actual_response = json.loads(response.data)
        expected_response = get_room_usage_analytics_invalid_location_response
        self.assertEquals(actual_response, expected_response)
