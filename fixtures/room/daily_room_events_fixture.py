daily_room_events_query = '''
query{
    analyticsForDailyRoomEvents(startDate:"jan 10 2019", endDate:"jan 10 2019"){
        day
        events{
            eventSummary
            startTime
            endTime
            roomName
            noOfParticipants
        }
    }
}
'''
daily_room_events_wrong_date_format_query = '''
query{
    analyticsForDailyRoomEvents(startDate:"10 jan 2019", endDate:"jan 10 2019"){
        day
        events{
            eventSummary
            startTime
            endTime
            roomName
            noOfParticipants
        }
    }
}
'''

daily_room_events_response = {
    "data": {
        "analyticsForDailyRoomEvents": [{
            "day": "Tue Jan 22 2019",
            "events": [
                {
                    'endTime': '14:00:00',
                    'eventSummary': 'SD sync',
                    'noOfParticipants': 3,
                    'roomName': 'Entebbe',
                    'startTime': '13:30:00'
                },
                {
                    'endTime': '14:45:00',
                    'eventSummary': 'Uzo<>Philip',
                    'noOfParticipants': 6,
                    'roomName': 'Entebbe',
                    'startTime': '14:00:00'
                }
            ]
        }]
    }
}

daily_events_wrong_date_format_response = {'errors': [
    {
        'message': "time data '10 jan 2019' does not match format '%b %d %Y'",
        'locations': [{'line': 3, 'column': 5}],
        'path': ['analyticsForDailyRoomEvents']}],
    'data': {
        'analyticsForDailyRoomEvents': None
}
}
