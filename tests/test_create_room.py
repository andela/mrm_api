import sys

from graphene.test import Client
from os.path import dirname, abspath
mrm_api = dirname(dirname(abspath(__file__)))
sys.path.insert(0, mrm_api)

from tests.base import BaseTestCase
from database import db_session


class TestCreateRoom(BaseTestCase):

    def test_room_creation(self):
        query = '''
                mutation {
                    createRoom(name: "Mbarara", type: "Meeting", capacity: 4, floorId: 1) {
                        room {
                            name
                            type
                            capacity
                            floorId
                        }
                    }
                }
            '''
        execute_query = self.client.execute(query, context_value={'session': db_session})
        
        expected_responese = {
            "data": {
                "createRoom": {
                    "room": {
                        "name": "Mbarara",
                        "type": "Meeting",
                        "capacity": 4,
                        "floorId": 1,
                    }
                }
            }
        }
        self.assertEqual(execute_query, expected_responese)