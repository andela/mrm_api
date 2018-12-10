import os
import sys
import json

from flask_testing import TestCase
from graphene.test import Client

from app import create_app
from schema import schema
from helpers.database import engine, db_session, Base
from api.location.models import Location
from api.block.models import Block
from api.floor.models import Floor
from api.wing.models import Wing
from api.room.models import Room
from api.room_resource.models import Resource
from api.user.models import User
from api.role.models import Role
from api.user_role.models import UsersRole
from api.devices.models import Devices
from api.office.models import Office
from fixtures.token.token_fixture import (
    ADMIN_TOKEN, USER_TOKEN, ADMIN_NIGERIA_TOKEN)


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
            admin_user = User(email="peter.walugembe@andela.com",
                              location="Kampala", name="Peter Walugembe",
                              picture="https://www.andela.com/walugembe")
            admin_user.save()
            lagos_admin = User(email="peter.adeoye@andela.com",
                               location="Lagos", name="Peter Adeoye",
                               picture="https://www.andela.com/adeoye")
            lagos_admin.save()
            role = Role(role="Admin")
            role.save()
            user_role = UsersRole(user_id=admin_user.id, role_id=role.id)
            user_role.save()
            lagos_role = UsersRole(user_id=lagos_admin.id, role_id=role.id)
            lagos_role.save()
            location = Location(name='Kampala', abbreviation='KLA')
            location.save()
            location_two = Location(name='Nairobi', abbreviation='NBO')
            location_two.save()
            location_three = Location(name='Lagos', abbreviation='LOS')
            location_three.save()
            office = Office(name="St. Catherines", location_id=location.id)
            office.save()
            office_two = Office(name="dojo", location_id=location_two.id)
            office_two.save()
            block = Block(name='EC', office_id=office.id)
            block.save()
            office_three = Office(name="Epic tower", location_id=location_three.id)  # noqa: E501
            office_three.save()
            floor = Floor(name='3rd', block_id=block.id)
            floor.save()
            floor_two = Floor(name='2nd', block_id=2)
            floor_two.save()
            wing = Wing(name="Naija", floor_id=floor_two.id)
            wing.save()
            wing_two = Wing(name="Big Apple", floor_id=floor_two.id)
            wing_two.save()
            room = Room(name='Entebbe',
                        room_type='meeting',
                        capacity=6,
                        floor_id=floor.id,
                        calendar_id='andela.com_3630363835303531343031@resource.calendar.google.com',  # noqa: E501
                        image_url="https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg")  # noqa: E501
            room.save()
            resource = Resource(name='Markers',
                                quantity=3,
                                room_id=room.id)
            resource.save()
            device = Devices(
                resource_id=resource.id,
                last_seen="2018-06-08T11:17:58.785136",
                date_added="2018-06-08T11:17:58.785136",
                name="Samsung",
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


class CommonTestCases(BaseTestCase):
    """Common test cases throught the code.
    This code is used to reduce duplication
    :params
        - admin_token_assert_equal
        - admin_token_assert_in
        - user_token_assert_equal
        - user_token_assert_in
    """

    def admin_token_assert_equal(self, query, expected_response):
        """
        Make a request with admin token and use assertEquals
        to compare the values

        :params
            - query, expected_response
        """
        headers = {"Authorization": "Bearer" + " " + ADMIN_TOKEN}
        response = self.app_test.post(
            '/mrm?query=' + query, headers=headers)
        actual_response = json.loads(response.data)
        self.assertEquals(actual_response, expected_response)

    def lagos_admin_token_assert_equal(self, query, expected_response):
        """
        Make a request with admin token and use assertEquals
        to compare the values

        :params
            - query, expected_response
        """
        headers = {"Authorization": "Bearer" + " " + ADMIN_NIGERIA_TOKEN}  # noqa E501
        response = self.app_test.post(
            '/mrm?query=' + query, headers=headers)
        actual_response = json.loads(response.data)
        self.assertEquals(actual_response, expected_response)

    def admin_token_assert_in(self, query, expected_response):
        """
        Make a request with admin token and use assertIn
        to compare the values

        :params
            - query, expected_response
        """
        headers = {"Authorization": "Bearer" + " " + ADMIN_TOKEN}
        response = self.app_test.post('/mrm?query=' + query, headers=headers)
        self.assertIn(expected_response, str(response.data))

    def lagos_admin_token_assert_in(self, query, expected_response):
        """
        Make a request with admin token and use assertIn
        to compare the values

        :params
            - query, expected_response
        """
        headers = {"Authorization": "Bearer" + " " + ADMIN_NIGERIA_TOKEN}  # noqa E501
        response = self.app_test.post('/mrm?query=' + query, headers=headers)
        self.assertIn(expected_response, str(response.data))

    def user_token_assert_equal(self, query, expected_response):
        """
        Make a request with user token and use assertEquals
        to compare the values

        :params
            - query, expected_response
        """
        headers = {"Authorization": "Bearer" + " " + USER_TOKEN}
        response = self.app_test.post(
            '/mrm?query=' + query, headers=headers)
        actual_response = json.loads(response.data)
        self.assertEquals(actual_response, expected_response)

    def user_token_assert_in(self, query, expected_response):
        """
        Make a request with user token and use assertIn
        to compare the values

        :params
            - query, expected_response
        """
        headers = {"Authorization": "Bearer" + " " + USER_TOKEN}
        response = self.app_test.post('/mrm?query=' + query, headers=headers)
        self.assertIn(expected_response, str(response.data))


def change_user_role_helper(func):
    def func_wrapper(self):
        headers = {"Authorization": "Bearer" + " " + USER_TOKEN}
        user = User(email='mrm@andela.com', name='this user',
                    location="Nairobi", picture='www.andela.com/user')
        user.save()
        user_role = UsersRole(user_id=user.id, role_id=1)
        user_role.save()
        db_session().commit()
        return headers
    return func_wrapper
