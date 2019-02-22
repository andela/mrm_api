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


class CalendarApi:
    def calendar_list(self, page_token):
        try:
            service = Credentials().set_api_credentials()
            calendars = service.calendarList().list(
                pageToken=page_token).execute()
        except Exception as exception:
            raise GraphQLError(exception)
        return calendars
