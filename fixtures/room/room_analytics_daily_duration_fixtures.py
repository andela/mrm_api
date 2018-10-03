null = None

get_daily_meetings_total_duration_query = '''
query {
    dailyDurationsOfMeetings(locationId:1, dayStart:"sep 10 2018"){
        dailyDurationaAnalytics{
            roomName
            count
            totalDuration
            events{
                durationInMinutes
                numberOfMeetings
            }
        }
    }
}
'''

get_daily_meetings_total_duration_response = {
    "data": {
        "dailyDurationsOfMeetings": {
            "dailyDurationaAnalytics": [
                {
                    "roomName": "Entebbe",
                    "count": 0,
                    "totalDuration": 0,
                    "events": []
                }
            ]
        }
    }
}
