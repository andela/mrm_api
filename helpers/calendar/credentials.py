import os

from apiclient.discovery import build
from httplib2 import Http
from graphql import GraphQLError
from oauth2client import file, client, tools  # noqa
from oauth2client.client import OAuth2WebServerFlow  # noqa


class Credentials():
    """Define api credentials
       :methods
           set_api_credentials
    """

    def set_api_credentials(self):
        """
        Setup the Calendar API
        """
        SCOPES = 'https://www.googleapis.com/auth/calendar'
        store = file.Storage('credentials.json')
        credentials = store.get()

        if not credentials or credentials.invalid:
            # Create a flow object. This object holds the client_id,
            # client_secret, and
            # SCOPES. It assists with OAuth 2.0 steps to get user
            # authorization and credentials.
            flow = OAuth2WebServerFlow(
                os.getenv('OOATH2_CLIENT_ID'),
                os.getenv('OOATH2_CLIENT_SECRET'),
                SCOPES)
            credentials = tools.run_flow(flow, store)
        api_key = os.getenv('API_KEY')
        service = build('calendar', 'v3', developerKey=api_key,
                        http=credentials.authorize(Http()))
        return service


def get_events_within_datetime_range(calendarId=None, timeMin=None,
                                     timeMax=None,
                                     singleEvents=None, orderBy=None):
    credentials = Credentials()
    service = credentials.set_api_credentials()
    events = service.events().list(calendarId=calendarId, timeMin=timeMin,
                                   timeMax=timeMax, singleEvents=singleEvents,
                                   orderBy=orderBy).execute()
    return events


def get_all_google_calendar_events(calendarId=None):
    credentials = Credentials()
    service = credentials.set_api_credentials()
    events = service.events().list(calendarId=calendarId).execute()
    return events


def get_google_api_calendar_list(pageToken=None):
    credentials = Credentials()
    try:
        service = credentials.set_api_credentials()
        calendars_list = service.calendarList().list(
            pageToken=pageToken).execute()
    except Exception as exception:
        raise GraphQLError(exception)
    return calendars_list
