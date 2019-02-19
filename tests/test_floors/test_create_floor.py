from tests.base import BaseTestCase, CommonTestCases

from helpers.database import engine, db_session
from fixtures.floor.create_floor_fixtures import (
    create_floor_mutation, create_floor_mutation_response,
    floor_name_empty_mutation, floor_mutation_duplicate_name,
    floor_mutation_duplicate_name_response,
    create_with_nonexistent_block_id,
    response_for_create_floor_with_database_error
)

import sys
import os
sys.path.append(os.getcwd())


class TestCreateFloor(BaseTestCase):
    def test_create_floors(self):
        """
        Testing for floor creation
        """
        CommonTestCases.admin_token_assert_equal(
          self,
          create_floor_mutation,
          create_floor_mutation_response
        )

    def test_floor_creation_with_name_empty(self):
        """
        Test floor creation with name field empty
        """
        CommonTestCases.admin_token_assert_in(
            self,
            floor_name_empty_mutation,
            "name is required field"
        )

    def test_floor_creation_with_duplicate_name(self):
        """
        Test floor creation with an already existing floor name
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            floor_mutation_duplicate_name,
            floor_mutation_duplicate_name_response
        )

    def test_for_error_if_bloock_id_is_non_existant(self):
        CommonTestCases.admin_token_assert_in(
            self,
            create_with_nonexistent_block_id,
            "Block not found")

    def test_database_connection_error(self):
        """
        test a user friendly message is returned to a user when database
        cannot be reached
        """
        BaseTestCase().tearDown()
        CommonTestCases.admin_token_assert_in(
            self,
            create_floor_mutation,
            "The database cannot be reached"
            )

    def test_create_floors_without_floors_relation(self):
        """
        Testing for floor creation without floor relation
        """
        db_session.remove()
        with engine.begin() as conn:
            conn.execute("DROP TABLE floors CASCADE")
        CommonTestCases.admin_token_assert_equal(
          self,
          create_floor_mutation,
          response_for_create_floor_with_database_error
        )
