from flask_testing import TestCase
from graphene.test import Client

from app import create_app
from schema import schema
from helpers.database import engine, db_session, Base
from api.location.models import Location
from api.block.models import Block
from api.floor.models import Floor
from api.room.models import Room

import sys
import os
sys.path.append(os.getcwd())
from api.user.models import User


class BaseTestCase(TestCase):

    def create_app(self):
        app = create_app('testing')
        self.base_url = 'https://127.0.0.1:5000/mrm'
        self.headers = {'content-type': 'application/json'}
        self.token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySW5mbyI6eyJpZCI6Ii1MQ2NlT05mdi1Gbm44OG1nV3ZWIiwiZW1haWwiOiJkZW5uaXMuamphZ3dlQGFuZGVsYS5jb20iLCJmaXJzdF9uYW1lIjoiRGVubmlzIiwibGFzdF9uYW1lIjoiSmphZ3dlIiwibmFtZSI6IkRlbm5pcyBKamFnd2UiLCJwaWN0dXJlIjoiaHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tLy1uWjg0d2R0LW1vRS9BQUFBQUFBQUFBSS9BQUFBQUFBQUFBYy81TlN4endZa2ZOUS9waG90by5qcGc_c3o9NTAiLCJyb2xlcyI6eyJBbmRlbGFuIjoiLUtpaWhmWm9zZVFlcUM2YldUYXUiLCJUZWNobm9sb2d5IjoiLUtYSDdpTUU0ZWJNRVhBRWM3SFAifX0sImV4cCI6MTUyOTA2NjkxNH0.dGgUNmSCJ6Q1iaMzs4m4diKbhHCAmI4m0f_zxFFTE7y53pv9hwXOPCgN4_8MT_JcRdd6wY16rlJN5z5soxJK7lr3TLMal9VS9Dyx4Dlb_6BkSFCRgGmlJQaX_71Gi6uNayW_ucLAWrHOqf3Mcptj-5JaJzBMS_7xDnc5HA-V5BI'
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
            db_session.commit()

            user = User(email='admin@mrm.com', name="Namuli")
            user.save()
            db_session().commit()
    
    def tearDown(self):
        app = self.create_app()
        with app.app_context():
            db_session.remove()
            Base.metadata.drop_all(bind=engine)
