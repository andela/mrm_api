null = None

get_daily_meetings_total_duration_query = '''
query {
    dailyDurationsOfMeetings(locationId:1, dayStart:"sep 10 2018"){
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

get_weekly_meetings_total_duration_query = '''
query {
    weeklyDurationsOfMeetings(locationId:1, weekStart:"Jan 3 2018", weekEnd:"Jan 9 2018"){  # noqa: E501
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

get_weekly_meetings_total_duration_response = {
    'data': {
        'weeklyDurationsOfMeetings': {
            'MeetingsDurationaAnalytics': [
                {
                    'roomName': 'Entebbe',
                    'count': 0,
                    'totalDuration': 0,
                    'events': []}]}}}
