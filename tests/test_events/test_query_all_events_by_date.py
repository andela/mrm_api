from tests.base import BaseTestCase, CommonTestCases

from fixtures.events.events_query_by_date_fixtures import (
    query_events,
    event_query_response,
    query_events_with_start_date_before_end_date,
    event_query_with_start_date_before_end_date_response,
    query_events_with_pagination,
    event_query_with_pagination_response,
    query_events_with_location,
    event_query_with_location_response,
    query_events_page_without_per_page,
    event_query_page_without_per_page_response,
    query_events_per_page_without_page,
    event_query_perPage_without_page_response,
    query_events_invalid_page,
    event_query_invalid_page_response,
    query_events_invalid_per_page,
    event_query_invalid_per_page_response,
    query_events_without_start_date,
    event_query_without_start_date_response,
    query_events_without_end_date,
    event_query_without_end_date_response,
    query_events_without_start_and_end_date,
    event_query_without_start_and_end_date_response,
    query_events_without_page_and_per_page,
    event_query_without_page_and_per_page_response
)
from tests.base import change_user_role_to_super_admin


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

    def test_query_events_with_start_date_before_end_date(self):
        """
        Test a user can query for all events with
        start date ahead of end date
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            query_events_with_start_date_before_end_date,
            event_query_with_start_date_before_end_date_response
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

    @change_user_role_to_super_admin
    def test_query_events_with_location(self):
        """
        Test a super_user can query for all events in all locations
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            query_events_with_location,
            event_query_with_location_response
        )

    def test_query_events_without_start_date(self):
        """
        Test a user can query for all events without
        start date
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            query_events_without_start_date,
            event_query_without_start_date_response
        )

    def test_query_events_without_end_date(self):
        """
        Test a user can query for all events without
        end date
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            query_events_without_end_date,
            event_query_without_end_date_response
        )

    def test_query_events_without_start_and_end_date(self):
        """
        Test a user can query for all events without
        start date and end date
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            query_events_without_start_and_end_date,
            event_query_without_start_and_end_date_response
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
