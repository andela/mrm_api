from flask_testing import TestCase
from graphene.test import Client

from app import create_app
from schema import schema
from helpers.database import engine, db_session, Base
from api.location.models import Location
from api.block.models import Block
from api.floor.models import Floor
from api.room.models import Room
from api.room_resource.models import Resource
from api.user.models import User
from api.role.models import Role
from api.user_role.models import UsersRole
from api.devices.models import Devices

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
        self.app_test = app.test_client()
        with app.app_context():
            Base.metadata.create_all(bind=engine)
            admin_user = User(email="patrick.walukagga@andela.com",
                              location="Kampala")
            admin_user.save()
            role = Role(role="Admin")
            role.save()
            user_role = UsersRole(user_id=admin_user.id, role_id=role.id)
            user_role.save()
            location = Location(name='Uganda', abbreviation='KLA')
            location.save()
            block = Block(name='EC', location_id=location.id)
            block.save()
            floor = Floor(name='3rd', block_id=block.id)
            floor.save()
            room = Room(name='Entebbe',
                        room_type='meeting',
                        capacity=6,
                        floor_id=floor.id,
                        calendar_id='andela.com_3835468272423230343935@resource.calendar.google.com',  # noqa: E501
                        image_url="https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg",
                        location="Uganda")  # noqa: E501
            room.save()
            resource = Resource(name='Markers',
                                quantity=3,
                                room_id=room.id)
            resource.save()
            device = Devices(
                resource_id=resource.id,
                last_seen="2018-06-08T11:17:58.785136",
                date_added="2018-06-08T11:17:58.785136",
                name="Samsung ",
                location="Nairobi",
                device_type="External Display"
            )
            device.save()
            db_session.commit()

    def tearDown(self):
        app = self.create_app()
        with app.app_context():
            db_session.remove()
            Base.metadata.drop_all(bind=engine)
