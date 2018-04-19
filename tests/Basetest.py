from flask_testing import TestCase
from graphene.test import Client
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from mrm_api.app import create_app
from mrm_api.schema import schema
from mrm_api.config import config
from mrm_api.database import engine, db_session, Base
from mrm_api.models import Floor, Location, Block,Room


class BaseTestCase(TestCase):
    
    def create_app(self):
        app = create_app(config_name='testing')
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
            room = Room(name='Entebbe', type_of_room='meeting', capacity=6, floor_id=floor.id)
            room.save()
            db_session.commit()
    
    def tearDown(self):
        app = self.create_app()
        with app.app_context():
            db_session.remove()
            Base.metadata.drop_all(bind=engine)