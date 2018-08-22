import sys
import os
import json

from tests.base import BaseTestCase
from fixtures.room.filter_room_fixtures import (
    filter_rooms_by_capacity,
    filter_rooms_by_capacity_response,
    filter_rooms_by_location,
    filter_rooms_by_location_response,
    filter_rooms_by_resources,
    filter_rooms_by_resources_response,
    filter_rooms_by_resources_location_capacity,
    filter_rooms_by_resources_location_capacityresponse,
    filter_rooms_by_non_existant_data,
    filter_rooms_by_non_existant_datay_response,
    filter_rooms_by_location_capacity,
    filter_rooms_by_location_capacity_response,
    filter_rooms_by_resources_capacity,
    filter_rooms_by_resources_capacity_response,
    filter_rooms_by_resources_location,
    filter_rooms_by_resources_location_response
)

from fixtures.token.token_fixture import (user_api_token)

sys.path.append(os.getcwd())


class RoomsFilter(BaseTestCase):
    def test_filter_room_by_capacity(self):
        api_headers = {'token': user_api_token}
        filter_room_by_capacity_query = self.app_test.post(
            '/mrm?query='+filter_rooms_by_capacity, headers=api_headers)
        actual_response = json.loads(filter_room_by_capacity_query.data)
        self.assertEquals(actual_response, filter_rooms_by_capacity_response)

    def test_filter_room_by_location(self):
        api_headers = {'token': user_api_token}
        filter_room_by_location_query = self.app_test.post(
            '/mrm?query='+filter_rooms_by_location, headers=api_headers)
        actual_response = json.loads(filter_room_by_location_query.data)
        self.assertEquals(actual_response, filter_rooms_by_location_response)

    def test_filter_room_by_resources(self):
        api_headers = {'token': user_api_token}
        filter_room_by_resources_query = self.app_test.post(
            '/mrm?query='+filter_rooms_by_resources, headers=api_headers)
        actual_response = json.loads(filter_room_by_resources_query.data)
        self.assertEquals(actual_response, filter_rooms_by_resources_response)

    def test_filter_room_by_location_capacity(self):
        api_headers = {'token': user_api_token}
        filter_room_by_location_capacity_query = self.app_test.post(
            '/mrm?query='+filter_rooms_by_location_capacity,
            headers=api_headers)
        actual_response = json.loads(filter_room_by_location_capacity_query.data)  # noqa: E501
        self.assertEquals(actual_response, filter_rooms_by_location_capacity_response)  # noqa: E501

    def test_filter_room_by_resources_capacity(self):
        api_headers = {'token': user_api_token}
        filter_room_by_resources_capacity_query = self.app_test.post(
            '/mrm?query='+filter_rooms_by_resources_capacity,
            headers=api_headers)
        actual_response = json.loads(filter_room_by_resources_capacity_query.data)  # noqa: E501
        self.assertEquals(actual_response, filter_rooms_by_resources_capacity_response)  # noqa: E501

    def test_filter_room_by_all(self):
        api_headers = {'token': user_api_token}
        filter_room_by_all = self.app_test.post(
            '/mrm?query='+filter_rooms_by_resources_location_capacity,
            headers=api_headers)
        actual_response = json.loads(filter_room_by_all.data)
        self.assertEquals(actual_response, filter_rooms_by_resources_location_capacityresponse)  # noqa: E501

    def test_filter_room_by_non_existant_data(self):
        api_headers = {'token': user_api_token}
        filter_room_by_nonexistant_query = self.app_test.post(
            '/mrm?query='+filter_rooms_by_non_existant_data,
            headers=api_headers)
        actual_response = json.loads(filter_room_by_nonexistant_query.data)
        self.assertEquals(actual_response, filter_rooms_by_non_existant_datay_response)  # noqa: E501

    def test_filter_room_by_resources_location(self):
        api_headers = {'token': user_api_token}
        filter_room_by_resources_capacity_query = self.app_test.post(
            '/mrm?query='+filter_rooms_by_resources_location,
            headers=api_headers)
        actual_response = json.loads(filter_room_by_resources_capacity_query.data)  # noqa: E501
        self.assertEquals(actual_response, filter_rooms_by_resources_location_response)  # noqa: E501
