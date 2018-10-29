import sys
import os

from tests.base import BaseTestCase, CommonTestCases
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
    filter_rooms_by_non_existant_data_response,
    filter_rooms_by_location_capacity,
    filter_rooms_by_location_capacity_response,
    filter_rooms_by_resources_capacity,
    filter_rooms_by_resources_capacity_response,
    filter_rooms_by_resources_location,
    filter_rooms_by_resources_location_response,
    filter_rooms_by_office,
    filter_rooms_by_office_capacity,
    filter_rooms_by_office_location,
    filter_rooms_by_office_capacity_location,
    filter_rooms_response
)

sys.path.append(os.getcwd())


class RoomsFilter(BaseTestCase):

    def test_filter_room_by_capacity(self):
        CommonTestCases.user_token_assert_equal(
            self,
            filter_rooms_by_capacity,
            filter_rooms_by_capacity_response
        )

    def test_filter_room_by_location(self):
        CommonTestCases.user_token_assert_equal(
            self,
            filter_rooms_by_location,
            filter_rooms_by_location_response
        )

    def test_filter_room_by_resources(self):
        CommonTestCases.user_token_assert_equal(
            self,
            filter_rooms_by_resources,
            filter_rooms_by_resources_response
        )

    def test_filter_room_by_location_capacity(self):
        CommonTestCases.user_token_assert_equal(
            self,
            filter_rooms_by_location_capacity,
            filter_rooms_by_location_capacity_response
        )

    def test_filter_room_by_resources_capacity(self):
        CommonTestCases.user_token_assert_equal(
            self,
            filter_rooms_by_resources_capacity,
            filter_rooms_by_resources_capacity_response
        )

    def test_filter_room_by_all(self):
        CommonTestCases.user_token_assert_equal(
            self,
            filter_rooms_by_resources_location_capacity,
            filter_rooms_by_resources_location_capacityresponse
        )

    def test_filter_room_by_non_existant_data(self):
        CommonTestCases.user_token_assert_equal(
            self,
            filter_rooms_by_non_existant_data,
            filter_rooms_by_non_existant_data_response
        )

    def test_filter_room_by_resources_location(self):
        CommonTestCases.user_token_assert_equal(
            self,
            filter_rooms_by_resources_location,
            filter_rooms_by_resources_location_response
        )

    def test_filter_room_by_office(self):
        CommonTestCases.user_token_assert_equal(
            self,
            filter_rooms_by_office,
            filter_rooms_response
        )

    def test_filter_room_by_office_capacity(self):
        CommonTestCases.user_token_assert_equal(
            self,
            filter_rooms_by_office_capacity,
            filter_rooms_response
        )

    def test_filter_room_by_office_location(self):
        CommonTestCases.user_token_assert_equal(
            self,
            filter_rooms_by_office_location,
            filter_rooms_response
        )

    def test_filter_room_by_office_capacity_location(self):
        CommonTestCases.user_token_assert_equal(
            self,
            filter_rooms_by_office_capacity_location,
            filter_rooms_response
        )
