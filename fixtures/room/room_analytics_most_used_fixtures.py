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
                        "count": 1
                    }
                ]
            }
        }
    }

get_most_used_room_per_week_query = '''
     {
        analyticsForMostUsedRooms(
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
get_most_used_room_per_week_response = {
   "data": {
        "analyticsForMostUsedRooms": {
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

get_most_used_room_without_event_query = '''
    {
        analyticsForMostUsedRooms(
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

get_most_used_room_without_event_response = {
    "data": {
        "analyticsForMostUsedRooms": {
            "analytics": [
                {
                    "roomName": "Entebbe",
                    "count": 1,
                    "events": [
                        {
                            'durationInMinutes': 45,
                            'numberOfMeetings': 1
                        }
                    ]}
            ]
        }
    }
}
