null = None

get_least_used_room_per_week_query = '''
    {
        analyticsForRoomLeastUsedPerWeek(
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
get_most_used_room_in_a_month_analytics_query = '''
    {
        mostUsedRoomPerMonthAnalytics(month:"Jul", year:2018)
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
get_least_used_room_per_week_query = '''
    {
        analyticsForRoomLeastUsedPerWeek(
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

get_most_used_room_per_week_query = '''
     {
        analyticsForRoomMostUsedPerWeek(
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

get_room_usage_analytics = '''
    {
    analyticsForMeetingsPerRoom(
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
        analyticsForLeastUsedRoomPerMonth(month:"Jul", year:2018)
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
        analyticsForLeastUsedRoomPerMonth(month:"Jul", year:2018)
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
get_most_used_room_per_week_response = {
   "data": {
        "analyticsForRoomMostUsedPerWeek": {
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


get_most_used_room_without_event_query = '''
    {
        analyticsForRoomMostUsedPerWeek(
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

get_most_used_room_without_event_response = {
    "data": {
        "analyticsForRoomMostUsedPerWeek": {
            "analytics": [
                {
                    "roomName": "Entebbe",
                    "count": 0,
                    "hasEvents": False,
                    "events": null}
            ]
        }
    }
}

analytics_for_least_used_room_day = '''
{
    analyticsForLeastUsedRoomPerDay(day:"Jul 11 2018"){
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
        "analyticsForLeastUsedRoomPerDay": {
            "analytics": [
                {
                    "roomName": "Entebbe",
                    "count": 0,
                    "events": null}
            ]
        }
    }
}
