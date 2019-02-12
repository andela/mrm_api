from tests.base import BaseTestCase, CommonTestCases
from fixtures.room.most_booked_room_least_booked_rooms_fixtures import (
    get_bottom_ten_rooms,
    get_top_ten_rooms,
    top_ten_response,
    bottom_ten_response,
    test_for_division_error
    )


class QueryRoomsAnalytics(BaseTestCase):

    def test_bottom_ten_most_used_rooms(self):
        CommonTestCases.admin_token_assert_equal(
            self,
            get_bottom_ten_rooms,
            bottom_ten_response
        )

    def test_top_ten_most_used_rooms(self):
        CommonTestCases.admin_token_assert_equal(
            self,
            get_top_ten_rooms,
            top_ten_response
        )

    def test_for_percentage_division_error(self):
        CommonTestCases.admin_token_assert_in(
            self,
            test_for_division_error,
            "There are no meetings"
        )
