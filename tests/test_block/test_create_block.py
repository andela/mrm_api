import sys
import os
from tests.base import BaseTestCase, CommonTestCases
from fixtures.block.create_block_fixtures import (
    create_block_query,
    create_block_response,
    block_mutation_query_without_name,
    create_block_with_non_existing_office,
    block_creation_with_duplicate_name,
    block_creation_with_duplicate_name_response,
    update_block,
    update_block_response,
    update_non_existent_block,
    update_non_existent_block_response,
    delete_block,
    delete_block_response,
    delete_non_existent_block,
    delete_non_existent_block_response,
    create_block_query_with_non_nairobi_id,
)


sys.path.append(os.getcwd())


class TestCreateBlock(BaseTestCase):

    def test_block_creation(self):
        """
        Testing for block creation

        """
        CommonTestCases.admin_token_assert_equal(
            self,
            create_block_query,
            create_block_response
        )

    def test_block_creation_with_name_empty(self):
        """
        Test block creation with name field empty
        """
        CommonTestCases.admin_token_assert_in(
            self,
            block_mutation_query_without_name,
            "name is required field"
        )

    def test_block_creation_with_non_existent_office(self):
        """
        Test block creation with non-existent office
        """
        CommonTestCases.admin_token_assert_in(
            self,
            create_block_with_non_existing_office,
            "Office not found"
        )

    def test_block_creation_with_duplicate_name(self):
        """
        Test block creation with an already existing room name
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            block_creation_with_duplicate_name,
            block_creation_with_duplicate_name_response
        )

    def test_update_block(self):
        """
        Test block creation with an already existing room name
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            update_block,
            update_block_response
        )

    def test_update_non_existent_block(self):
        """
        Test block creation with an already existing room name
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            update_non_existent_block,
            update_non_existent_block_response
        )

    def test_delete_block(self):
        """
        Test block creation with an already existing room name
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            delete_block,
            delete_block_response
        )

    def test_delete_non_existent_block(self):
        """
        Test block creation with an already existing room name
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            delete_non_existent_block,
            delete_non_existent_block_response
        )

    def test_only_create_block_in_nairobi(self):
        """
        Test whether you can only create  a block in Nairobi
        """
        CommonTestCases.admin_token_assert_in(
            self,
            create_block_query_with_non_nairobi_id,
            "You can only create block in Nairobi"
        )

    def test_databse_connection_error(self):
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
