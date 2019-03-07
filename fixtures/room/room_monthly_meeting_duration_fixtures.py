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
                        "totalDuration": 75,
                        "count": 2,
                        "events": [
                            {
                                "durationInMinutes": 30,
                                "numberOfMeetings": 1
                            },
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
