import sys
import os

from tests.base import BaseTestCase, CommonTestCases
from fixtures.office.office_fixtures import (
    office_mutation_query,
    office_mutation_query_Different_Location,
    office_mutation_query_non_existant_ID,
    office_mutation_query_duplicate_name,
    office_mutation_query_duplicate_name_responce)

sys.path.append(os.getcwd())


class TestCreateOffice(BaseTestCase):

    def test_office_creation(self):
        """
        Testing for office creation
        """
        CommonTestCases.admin_token_assert_in(
            self,
            office_mutation_query,
            "Office created but Emails not Sent"
        )

    def test_create_office_different_location(self):
        """
        Test creating office in different location
        """
        CommonTestCases.admin_token_assert_in(
            self,
            office_mutation_query_Different_Location,
            "You are not authorized to make changes in"
        )

    def test_office_creation_with_non_existant_ID(self):
        """
        Testing for office creation with non existant ID
        """
        CommonTestCases.admin_token_assert_in(
            self,
            office_mutation_query_non_existant_ID,
            "Location not found"
        )

    def test_office_creation_with_an_already_existent_name(self):
        """
        Testing for office creation with an already existing office name
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            office_mutation_query_duplicate_name,
            office_mutation_query_duplicate_name_responce
        )
