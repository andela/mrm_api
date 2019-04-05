from tests.base import BaseTestCase, CommonTestCases
from fixtures.structure.create_structure_fixtures import (
    office_structure_mutation_query,
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
