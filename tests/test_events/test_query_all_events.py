from tests.base import BaseTestCase, CommonTestCases
from fixtures.events.events_query_fixtures import (
    query_events,
    event_query_response
)


class TestEventsQuery(BaseTestCase):

    def test_query_events(self):
        """
        Test a user can query for all events
        """
        CommonTestCases.user_token_assert_equal(
            self,
            query_events,
            event_query_response
        )
