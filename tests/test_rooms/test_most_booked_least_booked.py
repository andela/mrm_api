from tests.base import BaseTestCase, CommonTestCases
from fixtures.room.most_booked_room_least_booked_rooms_fixtures import (
    get_bottom_ten_rooms,
    bottom_ten_response,
    get_top_ten_rooms,
    top_ten_response
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
