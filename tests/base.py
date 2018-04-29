from flask_testing import TestCase
from graphene.test import Client

from app import create_app
from schema import schema
from helpers.database import engine, db_session, Base
from api.location.models import Location
from api.block.models import Block
from api.floor.models import Floor
from api.room.models import Room
<<<<<<< HEAD
from api.room_resource.models import Resource
=======
from api.equipment.models import Equipment
>>>>>>> [Feature #156615347] Add tests

import sys
import os


sys.path.append(os.getcwd())


class BaseTestCase(TestCase):

    def create_app(self):
        app = create_app('testing')
        self.base_url = 'https://127.0.0.1:5000/mrm'
        self.headers = {'content-type': 'application/json'}
        self.client = Client(schema)
        return app

    def setUp(self):
        app = self.create_app()
        with app.app_context():
            Base.metadata.create_all(bind=engine)
            location = Location(name='Uganda', abbreviation='KLA')
            location.save()
            block = Block(name='EC', location_id=location.id)
            block.save()
            floor = Floor(name='3rd', block_id=block.id)
            floor.save()
            room = Room(name='Entebbe',
                        room_type='meeting',
                        capacity=6,
                        floor_id=floor.id)
            room.save()
            resource = Resource(name='Markers',
                                room_id=room.id)
            resource.save()
            db_session.commit()

    def tearDown(self):
        app = self.create_app()
        with app.app_context():
            db_session.remove()
            Base.metadata.drop_all(bind=engine)