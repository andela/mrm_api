"""This module containes test for the RoomSchedule Query
"""
from unittest.mock import patch

from tests.base import BaseTestCase, CommonTestCases
from helpers.calendar.calendar import get_events_mock_data
from fixtures.room.query_room_fixtures import (
    room_schedule_query,
    room_schedule_query_response,
    room_schedule_query_with_non_existant_calendar_id,
    room_schedule_of_non_existant_calendar_id_response
)


class QueryRoomSchedule(BaseTestCase):
    """This class deals with tests relating to querying room schedules
    and the google api integration
    funcs :
            - test_room_schedule
            - test_room_schedule_with_non_existant_calendar_id
    """

    @patch("helpers.calendar.events.get_google_calendar_events",
           spec=True)
    def test_room_schedule(self, mock_get_json):
        """
        This function tests the return types of the data received
        from RoomSchedule query
         - if it is a dictionary
         - if data is obtained
        """
        mock_get_json.return_value = get_events_mock_data()
        CommonTestCases.admin_token_assert_equal(
            self,
            room_schedule_query,
            room_schedule_query_response
        )

    def test_room_schedule_with_non_existant_calendar_id(self):
        """This function tests whether an error is raised if the calendarId is
            non existant.
        """
        query = self.client.execute(
            room_schedule_query_with_non_existant_calendar_id)
        self.assertNotEquals(
            query,
            room_schedule_of_non_existant_calendar_id_response
        )
