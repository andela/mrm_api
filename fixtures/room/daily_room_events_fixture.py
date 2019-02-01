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
        "analyticsForDailyRoomEvents": [
            {
                "day": "Thu Jan 10 2019",
                "events": [
                    {
                        "eventSummary": "Meeting",
                        "startTime": "12:30:00",
                        "endTime": "13:00:00",
                        "roomName": "Entebbe",
                        "noOfParticipants": 2
                    }
                ]
            }

        ]
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
