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
    filter_rooms_by_non_existant_data,
    filter_rooms_by_non_existant_data_response,
    filter_rooms_by_location_capacity,
    filter_rooms_by_location_capacity_response,
    filter_rooms_by_resources_capacity_location_response,
    filter_rooms_by_resources_location,
    filter_rooms_by_resources_location_response,
    filter_rooms_response,
    filter_rooms_by_resources_capacity,
    filter_rooms_by_tag,
    filter_rooms_by_tag_response,
    filter_rooms_by_invalid_tag,
    filter_rooms_by_invalid_tag_error_response
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

    def test_filter_room_by_resources_capacity_location(self):
        CommonTestCases.user_token_assert_equal(
            self,
            filter_rooms_by_resources_capacity,
            filter_rooms_by_resources_capacity_location_response
        )

    def test_filter_room_by_all(self):
        CommonTestCases.user_token_assert_equal(
            self,
            filter_rooms_by_resources_location_capacity,
            filter_rooms_response
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

    def test_filter_room_by_resources_capacity(self):
        CommonTestCases.user_token_assert_equal(
            self,
            filter_rooms_by_resources_capacity,
            filter_rooms_response
        )

    def test_filter_room_by_tag(self):
        """
        test admin can filter rooms by tag
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            filter_rooms_by_tag,
            filter_rooms_by_tag_response
        )

    def test_filter_room_by_invalid_tag(self):
        """
        test admin cannot filter rooms with  invalid tag_id
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            filter_rooms_by_invalid_tag,
            filter_rooms_by_invalid_tag_error_response
        )
