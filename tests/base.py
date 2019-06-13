import os
import sys
import json
import jwt

from flask_testing import TestCase
from graphene.test import Client
from datetime import datetime, timedelta
from alembic import command, config

from app import create_app
from schema import schema
from helpers.database import engine, db_session, Base
from api.location.models import Location
from api.room.models import Room
from api.room_resource.models import Resource
from api.user.models import User
from api.role.models import Role
from api.events.models import Events
from api.devices.models import Devices
from api.question.models import Question
from api.response.models import Response
from api.tag.models import Tag
from api.structure.models import Structure
from fixtures.token.token_fixture import (
    ADMIN_TOKEN, USER_TOKEN, ADMIN_NIGERIA_TOKEN)

sys.path.append(os.getcwd())


class BaseTestCase(TestCase):
    alembic_configuration = config.Config("./alembic.ini")

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

            command.stamp(self.alembic_configuration, 'head')
            command.downgrade(self.alembic_configuration, '-1')
            command.upgrade(self.alembic_configuration, 'head')

            admin_user = User(email="peter.walugembe@andela.com",
                              name="Peter Walugembe",
                              picture="https://www.andela.com/walugembe")
            admin_user.location = "Kampala"
            admin_user.save()
            lagos_admin = User(email="peter.adeoye@andela.com",
                               location="Lagos", name="Peter Adeoye",
                               picture="https://www.andela.com/adeoye")
            lagos_admin.save()
            global role
            role = Role(role="Admin")
            role.save()
            admin_user.roles.append(role)
            lagos_admin.roles.append(role)
            tag = Tag(name='Block-B',
                      color='green',
                      description='The description')
            tag.save()

            location = Location(name='Kampala',
                                abbreviation='KLA')
            location.save()
            location_two = Location(name='Nairobi',
                                    abbreviation='NBO')
            location_two.save()
            location_three = Location(name='Lagos',
                                      abbreviation='LOS')
            location_three.save()
            tag_two = Tag(name='Block-C',
                          color='blue',
                          description='The description')
            tag_two.save()
            room = Room(name='Entebbe',
                        room_type='meeting',
                        capacity=6,
                        location_id=location.id,
                        structure_id='851ae8b3-48dd-46b5-89bc-ca3f8111ad87',
                        calendar_id='andela.com_3630363835303531343031@resource.calendar.google.com',  # noqa: E501
                        image_url="https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg",  # noqa: E501
                        room_labels=["1st Floor", "Wing A"])
            room.save()
            room.room_tags.append(tag)
            room_2 = Room(name='Tana',
                        room_type='meeting',
                        capacity=14,
                        location_id=location.id,
                        structure_id='851ae8b3-48dd-46b5-89bc-ca3f8111ad87',
                        calendar_id='andela.com_3730313534393638323232@resource.calendar.google.com',  # noqa: E501
                        image_url="https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg",  # noqa: E501
                        room_labels=["1st Floor", "Wing B"])
            room_2.save()
            room_2.room_tags.append(tag)
            resource = Resource(name='Markers',
                                quantity=3)
            resource.save()
            device = Devices(
                last_seen="2018-06-08T11:17:58.785136",
                date_added="2018-06-08T11:17:58.785136",
                name="Samsung",
                location="Kampala",
                device_type="External Display",
                room_id=1
            )
            device.save()
            question_1 = Question(
                question_type="rate",
                question_title="Rating Feedback",
                question="How will you rate the brightness of the room",
                start_date="20 Nov 2018",
                end_date="28 Nov 2018",
                is_active=True
            )
            question_1.save()
            question_2 = Question(
                question_type="check",
                question_title="check Feedback",
                question="Is there anything missing in the room",
                start_date="20 Nov 2018",
                end_date="30 Nov 2018",
                is_active=True
            )
            event = Events(
                event_id="test_id5",
                room_id=1,
                event_title="Onboarding",
                start_time="2018-07-11T09:00:00Z",
                end_time="2018-07-11T09:45:00Z",
                number_of_participants=4,
                checked_in=False,
                cancelled=False)
            event.save()
            question_2.save()
            question_3 = Question(
                question_type="input",
                question_title="input Feedback",
                question="Any other suggestion",
                start_date="20 Nov 2018",
                end_date="28 Nov 2018"
            )
            question_3.save()
            response_1 = Response(
                question_id=1,
                room_id=1,
                rate=2,
                created_date=datetime.now() - timedelta(
                    days=1),
                resolved=False,
            )
            response_1.save()

            response_2 = Response(
                question_id=question_2.id,
                room_id=room.id,
                check=True,
                created_date=datetime.now() - timedelta(
                    days=1),
                resolved=True,
            )
            response_2.save()
            response_2.missing_resources.append(resource)
            structure = Structure(
                structure_id='b05fc5f2-b4aa-4f48-a8fb-30bdcc3fc968',
                level=1,
                name='Epic tower',
                parent_id="1",
                parent_title="parent_title",
                tag='Building',
                location_id=1,
                position=1,
            )
            structure.save()
            db_session.commit()

    def get_admin_location_id(self):
        payload = jwt.decode(ADMIN_TOKEN, verify=False)
        email = payload['UserInfo']['email']
        user = User.query.filter_by(email=email).first()
        location = Location.query.filter_by(name=user.location).first()
        return location.id

    def tearDown(self):
        app = self.create_app()
        with app.app_context():
            command.stamp(self.alembic_configuration, 'base')
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

    def single_structure_query_matches_admin_location(self, query):
        """
        Make a request with admin token to query a structure
        and assert it returns a structure in the admins location
        :params
            - query
        """
        headers = {"Authorization": "Bearer" + " " + ADMIN_TOKEN}
        response = self.app_test.post(
            '/mrm?query=' + query, headers=headers)
        admin_location_id = self.get_admin_location_id()
        response_data = json.loads(response.data)['data']
        actual_response = response_data['structureByStructureId']
        actual_location_id = actual_response['locationId']
        self.assertEquals(actual_location_id, admin_location_id)

    def structures_query_matches_admin_location(self, query):
        """
        Make a request with admin token to query structures
        and assert it returns structures in the admins location
        :params
            - query
        """
        headers = {"Authorization": "Bearer" + " " + ADMIN_TOKEN}
        response = self.app_test.post(
            '/mrm?query=' + query, headers=headers)
        admin_location_id = self.get_admin_location_id()
        all_structures = json.loads(response.data)['data']['allStructures']
        for structure in all_structures:
            self.assertEquals(structure['locationId'], admin_location_id)


def change_user_role_helper(func):
    def func_wrapper(self):
        headers = {"Authorization": "Bearer" + " " + USER_TOKEN}
        user = User(email='mrm@andela.com', name='this user',
                    location="Nairobi", picture='www.andela.com/user')
        user.save()
        user.roles.append(role)
        db_session().commit()
        return headers
    return func_wrapper


def change_test_user_role(func):
    def func_wrapper(self):
        user_role = Role(role='Default User')
        user_role.save()
        user = User(email='mrmtestuser@andela.com', name='Test user',
                    location="Lagos", picture='www.andela.com/testuser')
        user.save()
        user.roles.append(user_role)
        db_session().commit()
    return func_wrapper
