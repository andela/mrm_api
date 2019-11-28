from tests.base import BaseTestCase, CommonTestCases
from fixtures.events.events_query_by_date_fixtures import (
    query_events,
    query_events_with_start_date_before_end_date,
    query_events_with_pagination,
    query_events_page_without_per_page,
    query_events_per_page_without_page,
    query_events_invalid_page,
    query_events_invalid_per_page,
    query_events_without_start_date,
    query_events_without_end_date,
    query_events_without_start_and_end_date,
    query_events_without_page_and_per_page
)
from fixtures.events.events_query_by_date_responses_fixtures import (
    event_query_with_pagination_response,
    event_query_without_page_and_per_page_response
)


class TestEventsQuery(BaseTestCase):

    def test_query_events(self):
        """
        Test a user can query for all events
        """
        CommonTestCases.admin_token_assert_in(
            self,
            query_events,
            "Events do not exist for the date range"
        )

    def test_query_events_with_start_date_before_end_date(self):
        """
        Test a user can query for all events with
        start date ahead of end date
        """
        CommonTestCases.admin_token_assert_in(
            self,
            query_events_with_start_date_before_end_date,
            "Start date must be lower than end date"
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

    def test_query_events_without_start_date(self):
        """
        Test a user can query for all events without
        start date
        """
        CommonTestCases.admin_token_assert_in(
            self,
            query_events_without_start_date,
            "startDate argument missing"
        )

    def test_query_events_without_end_date(self):
        """
        Test a user can query for all events without
        end date
        """
        CommonTestCases.admin_token_assert_in(
            self,
            query_events_without_end_date,
            "endDate argument missing"
        )

    def test_query_events_without_start_and_end_date(self):
        """
        Test a user can query for all events without
        start date and end date
        """
        CommonTestCases.admin_token_assert_in(
            self,
            query_events_without_start_and_end_date,
            "Page does not exist"
        )

    def test_query_events_without_page_and_per_page(self):
        """
        Test a user can query for all events with
        page and per_page arguments
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            query_events_without_page_and_per_page,
            event_query_without_page_and_per_page_response
        )

    def test_query_events_missing_per_page(self):
        """
        Test to show that per_page is required if page is supplied
        """
        CommonTestCases.admin_token_assert_in(
            self,
            query_events_page_without_per_page,
            "perPage argument missing"
        )

    def test_query_events_missing_page(self):
        """
        Test to show that page is required if per_page is supplied
        """
        CommonTestCases.admin_token_assert_in(
            self,
            query_events_per_page_without_page,
            "page argument missing"
        )

    def test_query_events_invalid_page(self):
        """
        Test to show that page must be a positive integer
        """
        CommonTestCases.admin_token_assert_in(
            self,
            query_events_invalid_page,
            "page must be at least 1"
        )

    def test_query_events_invalid_per_page(self):
        """
        Test to show that per_page must be a positive integer
        """
        CommonTestCases.admin_token_assert_in(
            self,
            query_events_invalid_per_page,
            "perPage must be at least 1"
        )
