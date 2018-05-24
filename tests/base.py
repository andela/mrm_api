import sys
import os
sys.path.append(os.getcwd())

from flask_testing import TestCase
from graphene.test import Client
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from app import create_app
from schema import schema
from config import config
from helpers.database import engine, db_session, Base
from api.location.models import Location
from api.block.models import Block
from api.floor.models import Floor
from api.room.models import Room


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
            room = Room(
                name='Entebbe', 
                room_type='meeting', 
                capacity=6,
                calendar_id = 'andela.com_3835468272423230343935@resource.calendar.google.com',
                floor_id=floor.id
                )
            room.save()
            db_session.commit()
    
    def tearDown(self):
        app = self.create_app()
        with app.app_context():
            db_session.remove()
            Base.metadata.drop_all(bind=engine)
