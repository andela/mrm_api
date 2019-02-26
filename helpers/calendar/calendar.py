import json


def get_events_mock_data():
    with open('events.json', 'r') as outfile:
        events = json.load(outfile)
    return events


def get_calendar_list_mock_data():
    with open('calendar_list.json', 'r') as outfile:
        calendar_list = json.load(outfile)
    return calendar_list
