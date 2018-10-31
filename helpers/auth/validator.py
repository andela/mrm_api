import re
from graphql import GraphQLError
from helpers.calendar.credentials import Credentials


def check_office_name(office_name):
    return bool(re.match('^(epic\s?towers?||the\s?crest)$',  # noqa
                         office_name, re.IGNORECASE))


def assert_wing_is_required(office, kwargs):
    if re.match('^(epic\s?towers?)$', office, re.IGNORECASE):  # noqa
        if not kwargs.get('wing_id'):
            raise AttributeError("wing_id is required for this office")
    else:
        if kwargs.get('wing_id'):
            raise AttributeError("wing_id is not required for this office")


def assert_block_id_is_required(office, kwargs):
    if re.match('^(st\s?catherines?)$', office, re.IGNORECASE):  # noqa
        if not kwargs.get('block_id'):
            raise AttributeError("block_id is required for this office")
    else:
        if kwargs.get('block_id'):
            raise AttributeError("Block ID is not required for this office")


def verify_email(email):
    return bool(re.match('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$',  # noqa
                         email))


def verify_calendar_id(calendar_id):
    service = Credentials.set_api_credentials(Credentials)
    try:
        service.events().list(calendarId=calendar_id).execute()
        return True
    except Exception:
        return False


class ErrorHandler():
    '''Handles error'''

    def check_conflict(self, entity_name, entity):
        # Database integrity error
        raise GraphQLError(
            '{} {} already exists'.format(entity_name, entity))

    def foreign_key_conflict(self, entity_name, entity):
        # Database foreign key error
        raise GraphQLError(
            '{} {} does not exists'.format(entity_name, entity))

    def db_connection(self):
        # Database connection error
        raise GraphQLError('Error: Could not connect to Db')
