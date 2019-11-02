from tests.base import BaseTestCase, CommonTestCases
from fixtures.events.events_by_room_fixtures import (
    query_all_events_by_room_with_dates,
    query_all_events_by_room_with_dates_response,
    query_all_events_by_room_with_invalid_calendar_id,
    query_all_events_by_room_without_callendar_id,
    query_all_events_by_room_without_dates,
    query_all_events_by_room_without_dates_response

)


class TestEventsRoomQuery(BaseTestCase):

    def test_query_all_events_by_room_with_dates(self):
        """
        Test an admin or super admin can query
        for all events in a room with calendar Id,
        start date and end date
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            query_all_events_by_room_with_dates,
            query_all_events_by_room_with_dates_response
        )

    def test_query_all_events_by_room_without_dates(self):
        """
        Test an admin or super admin can query
        for all events in a room with the calendar Id only
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            query_all_events_by_room_without_dates,
            query_all_events_by_room_without_dates_response
        )

    def test_query_all_events_by_room_with_invalid_calendar_id(self):
        """
        Test an admin or super admin can query
        for all events with an invalid calendar Id
        or calendar Id with no events
        """
        CommonTestCases.admin_token_assert_in(
            self,
            query_all_events_by_room_with_invalid_calendar_id,
            "No rooms with the given CalendarId"
        )

    def test_query_all_events_by_room_without_callendar_id(self):
        """
        Test an admin or super admin can query
        for all events without a calendar Id
        """
        CommonTestCases.admin_token_assert_in(
            self,
            query_all_events_by_room_without_callendar_id,
            "Calendar Id missing"
        )
