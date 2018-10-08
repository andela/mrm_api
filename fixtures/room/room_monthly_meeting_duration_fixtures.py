get_monthly_meetings_total_duration_query = '''
    {
        monthlyDurationsOfMeetings(month:"Jul", year:2018, locationId:1)
        {
            MeetingsDurationaAnalytics {
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

get_monthly_meetings_total_duration_response = {
        "data": {
            "monthlyDurationsOfMeetings": {
                "MeetingsDurationaAnalytics": [
                    {
                        "roomName": "Entebbe",
                        "totalDuration": 0,
                        "count": 0,
                        "events": []
                    }
                ]
            }
        }
    }
