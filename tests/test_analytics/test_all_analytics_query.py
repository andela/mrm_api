from tests.base import (
    BaseTestCase,
    CommonTestCases,
    change_user_role_to_super_admin
)
from fixtures.analytics.query_all_analytics_fixtures import (
    all_analytics_query,
    all_analytics_query_response,
    all_analytics_query_invalid_locationid,
    analytics_query_for_date_ranges,
    all_analytics_query_response_super_admin_with_invalid_locationid
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

    @change_user_role_to_super_admin
    def test_all_analytics_query_super_admin(self):
        """
        Tests that a super admin user can query for analytics

        """

        CommonTestCases.admin_token_assert_equal(
            self,
            all_analytics_query,
            all_analytics_query_response
        )

        CommonTestCases.super_admin_token_assert_equal(
            self,
            all_analytics_query_invalid_locationid,
            all_analytics_query_response_super_admin_with_invalid_locationid
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
