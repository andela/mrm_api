null = None

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
