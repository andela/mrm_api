null = None

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
