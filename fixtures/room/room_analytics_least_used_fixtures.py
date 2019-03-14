null = None

get_least_used_room_per_week_query = '''
    {
        analyticsForLeastUsedRooms(
            startDate: "Sep 8 2018"
            endDate: "Sep 15 2018"
        )
        {
            analytics {
                roomName
                count
                hasEvents
                events {
                    durationInMinutes
                    numberOfMeetings
                }
            }
        }
    }
'''


get_least_used_room_per_week_response = {
    "data": {
        "analyticsForLeastUsedRooms": {
            "analytics": [
                {
                    "roomName": "Entebbe",
                    "count": 2,
                    "hasEvents": True,
                    "events": [
                        {
                            "durationInMinutes": 30,
                            "numberOfMeetings": 1
                        }
                    ]
                }
            ]
        }
    }
}

get_least_used_room_without_event_query = '''
    {
        analyticsForLeastUsedRooms(
            startDate: "Aug 8 2018"
            endDate: "Aug 12 2018"
        )
        {
            analytics {
                roomName
                count
                hasEvents
                events {
                    durationInMinutes
                    numberOfMeetings
                }
            }
        }
    }
'''

get_least_used_room_without_event_response = {
    "data": {
        "analyticsForLeastUsedRooms": {
            "analytics": [
                {
                    "roomName": "Entebbe",
                    "count": 2,
                    "hasEvents": True,
                    "events": [
                        {
                            "durationInMinutes": 30,
                            "numberOfMeetings": 1
                        }
                    ]
                }
            ]
        }
    }
}

get_room_usage_analytics = '''
    {
    analyticsForMeetingsPerRoom(
        startDate:"Sep 11 2018" endDate:"sep 12 2018"){
            analytics{
                roomName
                count
            }
        }
    }
'''

get_room_usage_anaytics_response = {
    "data": {
        "analyticsForMeetingsPerRoom": {
            "analytics": [{'roomName': 'Entebbe', 'count': 2}]
        }
    }
}

get_room_usage_no_meetings_analytics = '''
    {
    analyticsForMeetingsPerRoom(
        startDate:"Aug 12 2018" endDate:"Aug 12 2018"){
            analytics{
                roomName
                count
            }
        }
    }
'''

get_room_usage_no_meetings_anaytics_response = {
    "data": {
        "analyticsForMeetingsPerRoom": {
            "analytics": []
        }
    }
}

get_least_used_room_per_month = '''
    {
        analyticsForLeastUsedRooms(startDate:"Jul 1 2018", endDate:"Jul 31 2018")  # noqa: E501
        {
            analytics {
                roomName
                count
            }
        }
    }
'''

get_least_used_room_per_month_response = {
    'data': {
        'analyticsForLeastUsedRooms': {
            'analytics': [
                {
                    'roomName': 'Entebbe',
                    'count': 2
                }
            ]
        }
    }
}


analytics_for_least_used_room_day = '''
{
    analyticsForLeastUsedRooms(startDate:"Jul 11 2018"){
        analytics{
            roomName
            count
            events{
                durationInMinutes
                numberOfMeetings
            }
            }
        }
    }
'''

analytics_for_least_used_room_day_response = {
    "data": {
        "analyticsForLeastUsedRooms": {
            "analytics": [
                {
                    "roomName": "Entebbe",
                    "count": 2,
                    "events": [
                        {
                            "durationInMinutes": 30,
                            "numberOfMeetings": 1
                        }
                    ]
                }
            ]
        }
    }
}
