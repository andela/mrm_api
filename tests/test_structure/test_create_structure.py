from tests.base import BaseTestCase, CommonTestCases
from fixtures.structure.create_structure_fixtures import (
    office_structure_mutation_query,
    office_structure_mutation_with_duplicates,
    office_structure_mutation_response,
)


class TestCreateOfficeStructure(BaseTestCase):

    def test_structure_creation(self):
        """
        Tests an admin can create an office structure
        """

        CommonTestCases.admin_token_assert_equal(
            self,
            office_structure_mutation_query,
            office_structure_mutation_response
        )

    def test_structure_creation_payload_for_duplicates(self):
        """
        Tests that an admin cannot create an office structure with a
        payload of duplicated structure ids
        """

        CommonTestCases.admin_token_assert_in(
            self,
            office_structure_mutation_with_duplicates,
            'The office stuctures does not contain unique ids'
        )

    def test_structure_creation_for_duplicates(self):
        """
        Tests an admin cannot create an office structure twice
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            office_structure_mutation_query,
            office_structure_mutation_response
        )

        CommonTestCases.admin_token_assert_in(
            self,
            office_structure_mutation_query,
            'Office 1 already exists'
        )
