get_monthly_meetings_total_duration_query = '''
    {
        analyticsForMeetingsDurations(startDate:"Jul 1 2018", endDate:"Jul 31 2018")  # noqa: E501
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
            "analyticsForMeetingsDurations": {
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
