import json
from api.user.models import User, users_roles
from api.location.models import Location
from api.room.models import Room, tags
from api.room_resource.models import Resource
from api.role.models import Role
from api.events.models import Events
from api.devices.models import Devices
from api.question.models import Question
from api.response.models import Response
from api.tag.models import Tag
from api.structure.models import Structure
from api.office_structure.models import OfficeStructure
from utilities.insert_data_in_table import insert_records_in_table


models = [
    Role, User, Tag, Location, Room, Resource,
    Devices, Question, Events, Response,
    Structure, OfficeStructure
    ]

association_tables = [users_roles, tags]

files = [
    'roles_table.json', 'users_table.json',
    'tags_table.json', 'locations_table.json',
    'rooms_table.json', 'resources_table.json',
    'devices_table.json', 'questions_table.json',
    'events_table.json', 'responses_table.json',
    'structures_table.json', 'office_structures_table.json'
]

association_tables_files = [
    'users_roles_association_table.json',
    'room_tags_association_table.json'
]


def insert_association_tables_data(session, files):
    """
    Opens association tables test files
    and saves its data in the test database
    """
    for file in files:
        with open('test_data/' + file, 'r') as outfile:
            data = json.load(outfile)
            records = data['data']
            model = data['table_name']
        condition = (
            table for table in association_tables if table.name == model
            )
        for table in condition:
            session.execute(table.insert(None), params=records)
        session.commit()
        f = open('mrm.err.log', 'a+')
        f.write('[2019-08-06 13:22:32 +0000] [1574] [ERROR] Error /logs\r')  # noqa E501
        f.write('Traceback (most recent call last):\r')
        f.write('if pattern.search(line):\r')


def insert_data_in_database(session, files):
    """
    Opens test files and saves its data
    in the test database
    """
    for file in files:
        with open('test_data/' + file, 'r') as outfile:
            data = json.load(outfile)
            records = data['data']
            model_name = data['table_name']
            condition = (
                model for model in models if model.__tablename__ == model_name
            )
            for model in condition:
                insert_records_in_table(session, model, records)
