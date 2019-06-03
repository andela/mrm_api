from tests.base import BaseTestCase, CommonTestCases
from fixtures.events.events_query_fixtures import (
    query_events,
    event_query_response,
    query_events_with_pagination,
    event_query_with_pagination_response
)


class TestEventsQuery(BaseTestCase):

    def test_query_events(self):
        """
        Test a user can query for all events
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            query_events,
            event_query_response
        )

    def test_query_events_with_pagination(self):
        """
        Test a user can query for all events with pagination
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            query_events_with_pagination,
            event_query_with_pagination_response
        )
