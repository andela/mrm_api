null = None

most_used_room_in_a_month_analytics_invalid_location_query = '''
    {
        mostUsedRoomPerMonthAnalytics(month:"Dec", year:2018, locationId:19)
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
get_least_used_room_per_week_query = '''
    {
        analyticsForRoomLeastUsedPerWeek(
            locationId: 1,
            weekStart: "Sep 8 2018"
            weekEnd: "Sep 15 2018"
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

most_used_room_in_a_month_analytics_invalid_location_response = {
        "errors": [
            {
                "message": "No rooms in this location",
                "locations": [
                    {
                        "line": 3,
                        "column": 9
                    }
                ],
                "path": [
                    "mostUsedRoomPerMonthAnalytics"
                ]
            }
        ],
        "data": {
            "mostUsedRoomPerMonthAnalytics": null
        }
    }

get_most_used_room_in_a_month_analytics_query = '''
    {
        mostUsedRoomPerMonthAnalytics(month:"Jul", year:2018, locationId:1)
        {
            analytics {
                roomName
                count
            }
        }
    }
'''

get_most_used_room_in_a_month_analytics_response = {
        "data": {
            "mostUsedRoomPerMonthAnalytics": {
                "analytics": [
                    {
                        "roomName": "Entebbe",
                        "count": 0
                    }
                ]
            }
        }
    }

get_least_used_room_per_week_response = {
    "data": {
        "analyticsForRoomLeastUsedPerWeek": {
            "analytics": [
                {
                    "roomName": "Nairobi - 2nd Floor Block A Khartoum (1)",
                    "count": 5,
                    "hasEvents": True,
                    "events": [{
                        "durationInMinutes": 30,
                        "numberOfMeetings": 1
                    },
                        {
                        "durationInMinutes": 25,
                        "numberOfMeetings": 4
                    }
                    ]
                }
            ]
        }
    }
}

get_least_used_room_without_event_query = '''
    {
        analyticsForRoomLeastUsedPerWeek(
            locationId: 1,
            weekStart: "Aug 8 2018"
            weekEnd: "Aug 12 2018"
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
        "analyticsForRoomLeastUsedPerWeek": {
            "analytics": [
                {
                    "roomName": "Entebbe",
                    "count": 0,
                    "hasEvents": False,
                    "events": null
                }
            ]
        }
    }
}

get_room_usage_analytics = '''
    {
    analyticsForMeetingsPerRoom(locationId:1,
        dayStart:"Sep 11 2018" dayEnd:"sep 12 2018"){
            analytics{
                roomName
                count
            }
        }
    }
'''

get_least_used_room_per_month = '''
    {
        analyticsForLeastUsedRoomPerMonth(month:"Jul", year:2018, locationId:1)
        {
            analytics {
                roomName
                count
            }
        }
    }
'''
get_least_used_room_per_month = '''
    {
        analyticsForLeastUsedRoomPerMonth(month:"Jul", year:2018, locationId:1)
        {
            analytics {
                roomName
                count
            }
        }
    }
'''

get_room_usage_anaytics_respone = {
    "data": {
        "analyticsForMeetingsPerRoom": {
            "analytics": [{'roomName': 'Entebbe', 'count': 2}]
                    }
    }
}

get_least_used_room_per_month_response = {
    'data': {
        'analyticsForLeastUsedRoomPerMonth': {
            'analytics': [
                {
                    'roomName': 'Entebbe',
                    'count': 0
                }
            ]
        }
    }
}

get_least_used_room_per_month_response = {
    'data': {
        'analyticsForLeastUsedRoomPerMonth': {
            'analytics': [
                {
                    'roomName': 'Entebbe',
                    'count': 0
                }
            ]
        }
    }
}

get_room_usage_analytics_invalid_location = '''
{
    analyticsForMeetingsPerRoom(locationId:20,
    dayStart:"Sep 11 2018" dayEnd:"sep 12 2018"){
        analytics{
           roomName
           count
           }
        }
    }
'''

get_least_used_room_per_month_invalid_location = '''
    {
        analyticsForLeastUsedRoomPerMonth(month:"Jul", year:2018, locationId:99)
        {
            analytics {
                roomName
                count
            }
        }
    }
'''

get_room_usage_analytics_invalid_location_response = {
    'errors':
    [
        {
            'message': 'No rooms in this location',
            'locations': [{'line': 3, 'column': 5}],
            'path': ['analyticsForMeetingsPerRoom']
        }
    ],
        'data':
            {
                'analyticsForMeetingsPerRoom': None
            }
}

response_least_used_room_per_month_invalid_location = {
    "errors": [
        {
            "message": "No rooms in this location",
            "locations": [
                {
                    "line": 3,
                    "column": 9
                }
            ],
            "path": ["analyticsForLeastUsedRoomPerMonth"]
        }
    ],
    "data": {
        "analyticsForLeastUsedRoomPerMonth": null
        }
    }
