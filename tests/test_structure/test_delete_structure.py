import json

from tests.base import BaseTestCase, CommonTestCases
from fixtures.structure.delete_structure_fixtures import (
    delete_office_structures,
    delete_office_structures_with_invalid_id,
    delete_structures_expected_response
)
from fixtures.structure.create_structure_fixtures import (
    office_structure_mutation_query,
    office_structure_mutation_response
)
from fixtures.room.query_room_fixtures import (
    room_query_by_id,
    room_query_with_non_existant_id_response
)


class TestDeleteOfficeStructure(BaseTestCase):

    def test_structures_deletion(self):
        """
        Tests an admin can delete an office structure
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            office_structure_mutation_query,
            office_structure_mutation_response
        )
        CommonTestCases.admin_token_assert_equal(
            self,
            delete_office_structures,
            delete_structures_expected_response
        )

    def test_delete_non_existing_structures(self):
        """
        Tests that deleting non existing structure throws an
        error
        """
        CommonTestCases.admin_token_assert_in(
            self,
            delete_office_structures_with_invalid_id,
            'The structure invalid-id does not exist'
        )

    def test_rooms_related_to_structures_are_deleted(self):
        """
        Tests a room with a structure id that has been deleted
        the room is also deleted
        """
        CommonTestCases.admin_token_assert_equal(
            self,
            office_structure_mutation_query,
            office_structure_mutation_response
        )
        CommonTestCases.admin_token_assert_equal(
            self,
            delete_office_structures,
            delete_structures_expected_response
        )
        response = self.app_test.post('/mrm?query='+room_query_by_id)
        actual_response = json.loads(response.data)
        expected_response = room_query_with_non_existant_id_response
        self.assertEquals(
            actual_response["errors"][0]['message'], expected_response)
