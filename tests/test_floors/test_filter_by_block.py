from tests.base import BaseTestCase, CommonTestCases

from fixtures.floor.filter_by_block_fixtures import (
    filter_by_block_query,
    filter_by_block_response,
    filter_by_non_existent_block,
    error_response,

)


class TestFilterByBlock(BaseTestCase):
    def test_filter_rooms_in_block(self):
        CommonTestCases.admin_token_assert_equal(
            self,
            filter_by_block_query,
            filter_by_block_response
            )

    def test_filter_rooms_with_nonexistend_block(self):
        CommonTestCases.admin_token_assert_equal(
            self,
            filter_by_non_existent_block,
            error_response
            )
