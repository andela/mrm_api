import sys
import os
sys.path.append(os.getcwd())

from graphene.test import Client
from tests.base import BaseTestCase
from fixtures.room_resource.room_resource_fixtures import (
    resource_mutation_query, resource_mutation_response,
    resource_mutation_0_value_room_id_query, error_0_value_room_id,
    resource_mutation_empty_name_string_query, error_empty_name_string
)

from helpers.database import db_session
# from api.room.models import Room



class TestCreateRoomResource(BaseTestCase):

    def test_room_resource_creation(self):
        execute_query = self.admin_client.execute(
            resource_mutation_query,
            context_value={'session': db_session})
        
        expected_responese = resource_mutation_response
        self.assertEqual(execute_query, expected_responese)
    
    def test_room_resource_creation_name_error(self):
        execute_query = self.admin_client.execute(
            resource_mutation_empty_name_string_query,
            context_value={'session': db_session})
        
        expected_responese = error_empty_name_string
        self.assertEqual(execute_query, expected_responese)
    
    def test_room_resource_creation_room_id_error(self):
        execute_query = self.admin_client.execute(
            resource_mutation_0_value_room_id_query,
            context_value={'session': db_session})
        
        expected_responese = error_0_value_room_id
        self.assertEqual(execute_query, expected_responese)
