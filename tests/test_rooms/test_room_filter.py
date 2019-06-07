import sys
import os

from tests.base import BaseTestCase, CommonTestCases
from fixtures.room.filter_room_fixtures import (
    filter_rooms_by_capacity,
    filter_rooms_by_capacity_response,
    filter_rooms_by_location,
    filter_rooms_by_location_response,
    filter_rooms_by_location_capacity,
    filter_rooms_by_location_capacity_response,
    filter_rooms_by_wings_and_floors,
    filter_rooms_by_wings_and_floors_response,
    filter_rooms_by_non_existent_room_label,
    filter_rooms_by_non_existent_room_label_response,
    filter_rooms_by_room_labels,
    filter_rooms_by_room_labels_response,
    filter_rooms_by_location_room_labels,
    filter_rooms_by_resource,
    filter_rooms_by_location_resource
)
from fixtures.room.assign_resource_fixture import (
    assign_resource_mutation,
    assign_resource_mutation_response
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

    def test_filter_room_by_location_capacity(self):
        CommonTestCases.user_token_assert_equal(
            self,
            filter_rooms_by_location_capacity,
            filter_rooms_by_location_capacity_response
        )

    def test_filter_room_by_wings_and_floors(self):
        CommonTestCases.user_token_assert_equal(
            self,
            filter_rooms_by_wings_and_floors,
            filter_rooms_by_wings_and_floors_response
        )

    def test_room_filter_with_non_existent_room_label(self):
        CommonTestCases.user_token_assert_equal(
            self,
            filter_rooms_by_non_existent_room_label,
            filter_rooms_by_non_existent_room_label_response
        )

    def test_filter_room_by_location_room_label(self):
        CommonTestCases.user_token_assert_equal(
            self,
            filter_rooms_by_location_room_labels,
            filter_rooms_by_room_labels_response
        )

    def test_filter_room_by_room_label(self):
        CommonTestCases.user_token_assert_equal(
            self,
            filter_rooms_by_room_labels,
            filter_rooms_by_room_labels_response
        )

    def test_filter_room_by_resource(self):
        CommonTestCases.admin_token_assert_equal(
           self,
           assign_resource_mutation,
           assign_resource_mutation_response,
        )
        CommonTestCases.user_token_assert_equal(
            self,
            filter_rooms_by_resource,
            filter_rooms_by_room_labels_response
        )

    def test_filter_room_by_location_resource(self):
        CommonTestCases.admin_token_assert_equal(
           self,
           assign_resource_mutation,
           assign_resource_mutation_response,
        )
        CommonTestCases.user_token_assert_equal(
            self,
            filter_rooms_by_location_resource,
            filter_rooms_by_room_labels_response
        )
