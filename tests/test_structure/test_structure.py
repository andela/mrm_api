from tests.base import BaseTestCase, CommonTestCases
from fixtures.structure.structures_fixtures import (
    structure_query,
    expected_structure_query_response,
    structure_query_non_existant_structure_id,
    expected_error_non_existant_structure_id,
    structure_query_invalid_structure_id,
    expected_error_invalid_structure_id
)


class TestStructure(BaseTestCase):

    def test_query_structure_works(self):
        """
        Test that an admin can get a single office structure by
        supplying its structureId
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            structure_query,
            expected_structure_query_response
        )

    def test_structure_location_id_matches_admin_location(self):
        """
        Test that an admin can get a single office structure by
        supplying its structureId from their location only
        """
        CommonTestCases.single_structure_query_matches_admin_location(
            self,
            structure_query
        )

    def test_structure_with_non_existant_structure_id(self):
        """
        Test that no structure is returned if structureId is not provided
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            structure_query_non_existant_structure_id,
            expected_error_non_existant_structure_id
        )

    def test_structure_with_invalid_structure_id(self):
        """
        Test that no structure is returned if provided structureId is invalid
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            structure_query_invalid_structure_id,
            expected_error_invalid_structure_id
        )
