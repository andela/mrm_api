from tests.base import BaseTestCase, CommonTestCases
from fixtures.structure.update_structure_fixtures import (
    update_office_structure_mutation,
    update_office_structure_mutation_response,
    update_structure_invalid_id
)


class TestUpdateOfficeStructure(BaseTestCase):
    def test_office_structure_update(self):
        """
        Test that an admin can update an office structure
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            update_office_structure_mutation,
            update_office_structure_mutation_response
        )

    def test_update_non_existing_structures(self):
        """
        Tests that updating non existing structure throws an
        error
        """
        CommonTestCases.admin_token_assert_in(
            self,
            update_structure_invalid_id,
            'Structure not found'
        )
