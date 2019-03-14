null = None

get_least_used_room_per_week_query = '''
    {
        analyticsForLeastUsedRooms(
            startDate: "Jul 11 2018"
            endDate: "Jul 11 2018"
        )
        {
            analytics {
                roomName
                count
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
                    "count": 1,
                    "events": [
                        {
                            "durationInMinutes": 45,
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
            startDate: "Jul 11 2018"
            endDate: "Jul 11 2018"
        )
        {
            analytics {
                roomName
                count
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
                    "count": 1,
                    "events": [
                        {
                            "durationInMinutes": 45,
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
        startDate:"Jul 11 2018", endDate:"Jul 11 2018"){
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
            "analytics": [{'roomName': 'Entebbe', 'count': 1}]
        }
    }
}

get_least_used_room_per_month = '''
    {
        analyticsForLeastUsedRooms(startDate:"Jul 11 2018", endDate:"Jul 11 2018")  # noqa: E501
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
                    'count': 1
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
                    "count": 1,
                    "events": [
                        {
                            "durationInMinutes": 45,
                            "numberOfMeetings": 1
                        }
                    ]
                }
            ]
        }
    }
}
