"""This module containes test for the RoomSchedule Query
"""
from tests.base import BaseTestCase

from fixtures.room.room_fixtures import (
    room_schedule_query,
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

    def test_room_schedule(self):
        """
        This function tests the return types of the data received
        from RoomSchedule query
         - if it is a dictionary
         - if data is obtained
        """
        query = self.client.execute(room_schedule_query)
        assert type(query) is dict
        self.assertNotEquals(query, {})

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
