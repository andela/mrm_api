null = None

get_most_used_room_in_a_month_analytics_query = '''
    {
        analyticsForMostUsedRooms(startDate:"Jul 1 2018", endDate:"Jul 31 2018")
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
            "analyticsForMostUsedRooms": {
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
        analyticsForMostUsedRooms(
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
get_most_used_room_per_week_response = {
   "data": {
        "analyticsForMostUsedRooms": {
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
        analyticsForMostUsedRooms(
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

get_most_used_room_without_event_response = {
    "data": {
        "analyticsForMostUsedRooms": {
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
