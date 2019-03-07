import re
from graphql import GraphQLError
from helpers.calendar.credentials import (
    get_google_calendar_events)

from api.location.models import Location


def verify_email(email):
    return bool(re.match('^[a-zA-Z0-9_.+-]+@andela+\.com+$', email))  # noqa


def verify_calendar_id(calendar_id):
    try:
        get_google_calendar_events(calendarId=calendar_id)
        return True
    except Exception:
        return False


def verify_location_id(kwargs):
    location_id = kwargs.get('location_id')
    if location_id and not Location.query.filter_by(id=location_id,
                                                    state="active").first():
        raise AttributeError("Location Id does not exist")


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
