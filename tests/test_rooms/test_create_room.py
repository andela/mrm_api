from tests.base import BaseTestCase
from fixtures.room.room_fixtures import (
    room_mutation_query, room_mutation_response
)
from helpers.database import db_session

import sys
import os
sys.path.append(os.getcwd())


class TestCreateRoom(BaseTestCase):

    def test_room_creation(self):
        """
        Testing for room creation
        """
        execute_query = self.client.execute(
            room_mutation_query,
            context_value={'session': db_session})

        expected_responese = room_mutation_response
        self.assertEqual(execute_query, expected_responese)
