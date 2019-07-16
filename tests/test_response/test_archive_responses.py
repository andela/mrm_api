from tests.base import BaseTestCase, CommonTestCases
from fixtures.response.archive_response_fixtures import (
    archive_response_mutation,
    archive_response_response,
    archive_non_existing_response_mutation,
    archive_non_existing_response_response,
    archive_unresolved_response_mutation,
    archive_unresolved_response_response,
    filter_archived_responses_query,
    filter_archived_responses_response
)


class TestArchiveResponse(BaseTestCase):
    def test_archive_resolved_response(self):
        """
        Tests an admin can archive a resolved response
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            archive_response_mutation,
            archive_response_response)

    def test_archive_unresolved_response(self):
        """
        Tests an admin cannot archive an unresolved response
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            archive_unresolved_response_mutation,
            archive_unresolved_response_response
        )

    def test_archive_non_existing_response(self):
        """
        Tests an admin cannot archive a non-existing response
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            archive_non_existing_response_mutation,
            archive_non_existing_response_response
        )

    def test_fetch_archived_responses(self):
        """
        Tests an admin can retrieve archived responses
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            filter_archived_responses_query,
            filter_archived_responses_response
        )
