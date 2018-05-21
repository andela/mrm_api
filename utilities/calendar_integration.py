"""
This module handles MRM-Converge Google Clandar Intergrations.
It also holds utility functions for interacting with 
"""
from __future__ import print_function
import os
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import datetime
from oauth2client.client import OAuth2WebServerFlow




def set_calendar_API():
    #  Setup the Calendar API
    SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
    store = file.Storage('credentials.json')
    credentials = store.get()

    if not credentials or credentials.invalid:
        # credentials.
        flow = OAuth2WebServerFlow(
            os.getenv('OOATH2_CLIENT_ID'), 
            os.getenv('OOATH2_CLIEN#T_SECRET'), 
            SCOPES)
        credentials = tools.run_flow(flow, store)
    api_key = os.getenv('API_KEY')
    service = build('calendar', 'v3', developerKey=api_key, http=credentials.authorize(Http()))
    return service


# Call the Calendar API


def calendar_time_schedule(calendar_id,days,service):
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time

    new_time = (datetime.datetime.now() + datetime.timedelta(days=days)).isoformat() + 'Z'

    events_result = service.events().list(
        calendarId=calendar_id, 
        timeMin=now,
        timeMax= new_time,
        singleEvents=True,
        orderBy='startTime').execute()

    calendar_events = events_result.get('items', [])
    if not calendar_events:
        return('No upcoming events found.')
    for event in calendar_events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        return(start,event.get("summary"))
