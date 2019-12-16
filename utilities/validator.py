import re
from helpers.calendar.credentials import (
    get_google_calendar_events)

from api.location.models import Location
from api.tag.models import Tag as TagModel
from api.bugsnag_error import return_error


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
        return_error.report_errors_bugsnag_and_graphQL(
            "Location Id does not exist")


def verify_tag_id(tag_id):
    """
    Function to validate tag ID
    when creating a node or a child
    """
    tag_id = TagModel.query.filter_by(id=tag_id).first()
    if not tag_id:
        return_error.report_errors_bugsnag_and_graphQL(
            "Tag ID Provided does not exist")


class ErrorHandler():
    '''Handles error'''

    def check_conflict(self, entity_name, entity):
        # Database integrity error
        return_error.report_errors_bugsnag_and_graphQL(
            '{} {} already exists'.format(entity_name, entity))

    def foreign_key_conflict(self, entity_name, entity):
        # Database foreign key error
        return_error.report_errors_bugsnag_and_graphQL(
            '{} {} does not exists'.format(entity_name, entity))

    def db_connection(self):
        # Database connection error
        return_error.report_errors_bugsnag_and_graphQL(
            'Error: Could not connect to Db')
