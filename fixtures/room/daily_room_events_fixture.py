daily_room_events_query = '''
query{
    analyticsForDailyRoomEvents(startDate:"Jul 11 2018", endDate:"Jul 11 2018"){
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
    analyticsForDailyRoomEvents(startDate:"10 jan 2019", endDate:"10 jan 2019"){
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
            "day": "Wed Jul 11 2018",
            "events": [
                {
                    'endTime': '09:45:00',
                    'eventSummary': 'Onboarding',
                    'noOfParticipants': 4,
                    'roomName': 'Entebbe',
                    'startTime': '09:00:00'
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
