from tests.base import BaseTestCase, CommonTestCases
from fixtures.events.events_query_fixtures import (
    query_events,
    event_query_response,
    query_events_with_pagination,
    event_query_with_pagination_response,
    query_events_page_without_per_page,
    event_query_page_without_per_page_response,
    query_events_per_page_without_page,
    event_query_perPage_without_page_response,
    query_events_invalid_page,
    event_query_invalid_page_response,
    query_events_invalid_per_page,
    event_query_invalid_per_page_response
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

    def test_query_events_missing_per_page(self):
        """
        Test to show that per_page is required if page is supplied
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            query_events_page_without_per_page,
            event_query_page_without_per_page_response
        )

    def test_query_events_missing_page(self):
        """
        Test to show that page is required if per_page is supplied
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            query_events_per_page_without_page,
            event_query_perPage_without_page_response
        )

    def test_query_events_invalid_page(self):
        """
        Test to show that page must be a positive integer
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            query_events_invalid_page,
            event_query_invalid_page_response
        )

    def test_query_events_invalid_per_page(self):
        """
        Test to show that per_page must be a positive integer
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            query_events_invalid_per_page,
            event_query_invalid_per_page_response
        )
