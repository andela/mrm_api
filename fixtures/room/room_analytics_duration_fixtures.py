null = None

get_daily_meetings_total_duration_query = '''
query {
    analyticsForMeetingsDurations(startDate:"sep 10 2018"){
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
        "analyticsForMeetingsDurations": {
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
    analyticsForMeetingsDurations(startDate:"Jan 3 2018", endDate:"Jan 9 2018"){  # noqa: E501
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
        'analyticsForMeetingsDurations': {
            'MeetingsDurationaAnalytics': [
                {
                    'roomName': 'Entebbe',
                    'count': 0,
                    'totalDuration': 0,
                    'events': []}]}}}
