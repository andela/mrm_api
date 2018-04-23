import sys
import os
sys.path.append(os.getcwd())

from graphene.test import Client
from os.path import dirname, abspath
mrm_api = dirname(dirname(abspath(__file__)))
sys.path.insert(0, mrm_api)

from tests.base import BaseTestCase
from fixtures.room.room_fixtures import (
    room_mutation_query, room_mutation_response
)
from helpers.database import db_session

class TestCreateRoom(BaseTestCase):

    def test_room_creation(self):
        execute_query = self.admin_client.execute(
            room_mutation_query,
            context_value={'session': db_session})
        
        expected_responese = room_mutation_response
        self.assertEqual(execute_query, expected_responese)
