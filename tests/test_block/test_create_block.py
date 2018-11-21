import sys
import os
from tests.base import BaseTestCase, CommonTestCases
from fixtures.block.create_block_fixtures import (
    create_block_query,
    create_block_response,
    block_mutation_query_without_name,
    create_block_with_non_existing_office,
    block_creation_with_duplicate_name,
    block_creation_with_duplicate_name_response
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
