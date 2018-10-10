null = None

get_daily_meetings_total_duration_query = '''
query {
    dailyDurationsOfMeetings(dayStart: "sep 10 2018"){
        MeetingsDurationaAnalytics{
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
            "MeetingsDurationaAnalytics": [
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
