"""This module deals with testing Calendar Integration with focus on
    googleapi credentials
"""
from helpers.calendar.events import RoomSchedules
from tests.base import BaseTestCase

import sys
import os
sys.path.append(os.getcwd())


class TestEvents(BaseTestCase):
    """ This class tests for the google api credentials
    func :
        - test_response_events
    """
    def test_response_event(self):
        """ This function tests for type of response
        of the response to see if its a googleapi object
        RoomSchedule function
        """
        calendarId = 'andela.com_3730363934383237313139@resource.calendar.google.com'  # noqa: E501
        response = RoomSchedules.get_room_schedules(self, calendarId, 7)
        assert type(response) is list
        self.assertNotEquals(response, [])
