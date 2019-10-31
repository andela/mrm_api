import sys
import os
from tests.base import BaseTestCase, CommonTestCases
from fixtures.events.book_event_fixtures import (
    book_event_mutation,
    book_event_mutation_no_room,
    book_event_mutation_no_start_date,
    book_event_mutation_no_start_time,
    book_event_mutation_no_title,
    book_event_mutation_no_time_Zone
)

sys.path.append(os.getcwd())


class TestBookEvent(BaseTestCase):

    def test_user_book_event(self):
        """
        Test that a user can book an event via the converge app
        on the Googe Calendar
        """
        CommonTestCases.user_token_assert_in(
            self,
            book_event_mutation,
            'Event created successfully'
        )

    def test_event_date_validation(self):
        """
        Test that a user can not book an event without
        providing an event start date
        """
        CommonTestCases.user_token_assert_in(
            self,
            book_event_mutation_no_start_date,
            'start_date can not be empty'
        )

    def test_event_start_time_validation(self):
        """
        Test that a user can not book an event without
        providing an event start time
        """
        CommonTestCases.user_token_assert_in(
            self,
            book_event_mutation_no_start_time,
            'start_time can not be empty'
        )

    def test_event_title_validation(self):
        """
        Test that a user can not book an event without
        providing an event title
        """
        CommonTestCases.user_token_assert_in(
            self,
            book_event_mutation_no_title,
            'event_title can not be empty'
        )

    def test_event_room_validation(self):
        """
        Test that a user can not book an event without
        providing an event room/location
        """
        CommonTestCases.user_token_assert_in(
            self,
            book_event_mutation_no_room,
            'room can not be empty'
        )

    def test_event_time_zone_validation(self):
        """
        Test that a user can not book an event
        without providing a time_zone
        """
        CommonTestCases.user_token_assert_in(
            self,
            book_event_mutation_no_time_Zone,
            "time_zone can not be empty"
        )
