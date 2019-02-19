import sys
import os
from tests.base import BaseTestCase, CommonTestCases
from helpers.database import engine, db_session
from fixtures.events.event_checkin_fixtures import (
    event_checkin_mutation,
    cancel_event_mutation,
)

sys.path.append(os.getcwd())


class TestEventCheckin(BaseTestCase):
    def test_checkin_without_events_model(self):
        """
        test a user friendly message is returned to a user when database
        cannot be reached
        """
        db_session.remove()
        with engine.begin() as conn:
            conn.execute("DROP TABLE locations CASCADE")
            conn.execute("DROP TABLE events CASCADE")
        CommonTestCases.admin_token_assert_in(
            self,
            event_checkin_mutation,
            "There seems to be a database connection error",
        )

    def test_cancel_without_events_model(self):
        """
        test a user friendly message is returned to a user when database
        cannot be reached
        """
        db_session.remove()
        with engine.begin() as conn:
            conn.execute("DROP TABLE locations CASCADE")
            conn.execute("DROP TABLE events CASCADE")
        CommonTestCases.admin_token_assert_in(
            self,
            cancel_event_mutation,
            "There seems to be a database connection error",
        )
