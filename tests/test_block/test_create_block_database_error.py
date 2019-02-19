import sys
import os
from helpers.database import engine, db_session
from tests.base import BaseTestCase, CommonTestCases
from fixtures.block.create_block_fixtures import (
    create_block_query,
    update_block,
    delete_block,
    response_for_create_block_with_database_error,
    response_for_delete_block_with_database_error,
    response_for_update_block_with_database_error
)


sys.path.append(os.getcwd())


class TestCreateBlock(BaseTestCase):

    def test_delete_block_without_block_table(self):
        """
        test block creation without block relation
        """
        db_session.remove()
        with engine.begin() as conn:
            conn.execute("DROP TABLE blocks CASCADE")
        CommonTestCases.admin_token_assert_equal(
            self,
            delete_block,
            response_for_delete_block_with_database_error
        )

    def test_update_block_without_block_table(self):
        """
        test block creation without block relation
        """
        db_session.remove()
        with engine.begin() as conn:
            conn.execute("DROP TABLE blocks CASCADE")
        CommonTestCases.admin_token_assert_equal(
            self,
            update_block,
            response_for_update_block_with_database_error
        )

    def test_create_block_without_block_table(self):
        """
        test block creation without block relation
        """
        db_session.remove()
        with engine.begin() as conn:
            conn.execute("DROP TABLE offices CASCADE")
            conn.execute("DROP TABLE blocks CASCADE")
        CommonTestCases.admin_token_assert_equal(
            self,
            create_block_query,
            response_for_create_block_with_database_error
        )
