import sys
import os
sys.path.append(os.getcwd())

from graphene.test import Client
from os.path import dirname, abspath
mrm_api = dirname(dirname(abspath(__file__)))
sys.path.insert(0, mrm_api)

from tests.base import BaseTestCase
from fixtures.room_resource.get_room_resource_fixtures import (
    resource_query, resource_query_response
)

from helpers.database import db_session
from api.room_resource.models import Resource



class TestGetRoomResource(BaseTestCase):

    def test_get_room_resource_list(self):
        room_resource = Resource(name="Markers", room_id=1)
        room_resource.save()
        db_session().commit()

        execute_query = self.admin_client.execute(
            resource_query,
            context_value={'session': db_session})
        
        expected_responese = resource_query_response
        self.assertEqual(execute_query, expected_responese)
