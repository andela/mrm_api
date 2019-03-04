import sys
import os
from tests.base import BaseTestCase, CommonTestCases
from fixtures.block.create_block_fixtures import (
    create_block_query,
    update_block,
    delete_block,
)


sys.path.append(os.getcwd())


class TestCreateBlockError(BaseTestCase):

    def test_database_connection_error(self):
        """
        test a user friendly message is returned to a user when database
        cannot be reached
        """
        BaseTestCase().tearDown()
        CommonTestCases.admin_token_assert_in(
            self,
            create_block_query,
            "The database cannot be reached"
        )
        CommonTestCases.admin_token_assert_in(
            self,
            update_block,
            "The database cannot be reached"
        )
        CommonTestCases.admin_token_assert_in(
            self,
            delete_block,
            "The database cannot be reached"
        )
