from tests.base import BaseTestCase, CommonTestCases
from fixtures.analytics.query_all_analytics_fixtures import (
    all_analytics_query,
    all_analytics_query_response,
    analytics_query_for_date_ranges
)


class TestAllAnalytics(BaseTestCase):

    def test_all_analytics_query(self):
        """
        Tests a user can query for analytics
        """

        CommonTestCases.admin_token_assert_equal(
            self,
            all_analytics_query,
            all_analytics_query_response
        )

    def test_analytics_query_for_date_range(self):
        """
        Tests the date range to ensure start
        date is smaller than end date

        """

        CommonTestCases.admin_token_assert_in(
            self,
            analytics_query_for_date_ranges,
            "Earlier date should be lower than later date"
        )
