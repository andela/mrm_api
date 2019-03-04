import sys
import os

from tests.base import BaseTestCase, CommonTestCases
from fixtures.office.update_delete_office_fixture import (
    update_office_in_another_location_query,
    update_office_with_wrong_ID_query,
    update_office_with_same_Name_query,
    update_office_query,
    office_mutation_response
    )
sys.path.append(os.getcwd())


class TestUpdateOffice(BaseTestCase):

    def test_update_office(self):
        """
        Test updating an existing office
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            update_office_query,
            office_mutation_response
        )

    def test_updating_non_existant_office(self):
        """
        Test updating a non existing office
        """
        CommonTestCases.admin_token_assert_in(
            self,
            update_office_with_wrong_ID_query,
            "Office not found"
        )

    def test_updating_office_name_with_an_existing_name(self):
        """
        Test updating office name with an already existing name
        """
        CommonTestCases.admin_token_assert_in(
            self,
            update_office_with_same_Name_query,
            "Action Failed"
        )

    def test_updating_office_in_another_location(self):
        """
        Test updating office in another location
        """
        CommonTestCases.admin_token_assert_in(
            self,
            update_office_in_another_location_query,
            "You are not authorized to make changes in"
        )

    def test_database_connection_error(self):
        """
        test a user friendly message is returned to a user when database
        cannot be reached
        """
        BaseTestCase().tearDown()
        CommonTestCases.admin_token_assert_in(
            self,
            update_office_query,
            "The database cannot be reached"
            )
