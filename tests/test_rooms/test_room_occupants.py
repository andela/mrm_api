"""This module containes test for the RoomSchedule Query
"""
from tests.base import BaseTestCase

from fixtures.room.room_fixtures import (
    room_occupants_query,
    room_occupants_query_with_non_existant_calendar_id,
    room_occupants_of_non_existant_calendar_id_response
)


class TestRoomOccupants(BaseTestCase):
    """This class deals with tests for querying room occupants
    and the google api integration
    funcs :
            - test_room_occupants
            - test_room_occupants_with_non_existant_calendar_id
    """

    def test_room_occupants(self):
        """
        This function tests the return types of the data received
        from RoomSchedule query
         - if it is a dictionary
         - if data is obtained
        """
        query = self.client.execute(room_occupants_query)
        assert isinstance(query, dict)
        self.assertNotEquals(query, {})

    def test_room_occupants_with_non_existant_calendar_id(self):
        """This function tests whether an error is raised if the calendarId is
            non existant.
        """
        query = self.client.execute(
            room_occupants_query_with_non_existant_calendar_id)
        self.assertNotEquals(
            query,
            room_occupants_of_non_existant_calendar_id_response
        )
