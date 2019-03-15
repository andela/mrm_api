null = None
true = True
false = False

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
                    "count": 2,
                    "totalDuration": 75,
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

meetings_total_duration_query_for_a_future_date = '''
query {
    analyticsForMeetingsDurations(startDate:"sep 10 6080"){
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
                    'count': 2,
                    'totalDuration': 75,
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
                    }]}}}

get_paginated_meetings_total_duration_query = '''
query {
    analyticsForMeetingsDurations(startDate:"sep 10 2018", perPage:1, page:1){
    hasPrevious,
    hasNext,
    pages,
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

get_paginated_meetings_total_duration_response = {
  "data": {
    "analyticsForMeetingsDurations": {
      "hasPrevious": false,
      "hasNext": false,
      "pages": 1,
      "MeetingsDurationaAnalytics": [
        {
          "roomName": "Entebbe",
          "count": 2,
          "totalDuration": 75,
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

get_paginated_meetings_total_duration_query_invalid_page = '''
query {
    analyticsForMeetingsDurations(startDate:"sep 10 2018", perPage:1, page:100){
    hasPrevious,
    hasNext,
    pages,
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

get_paginated_meetings_total_duration_invalid_page_result = {
    "errors": [{
        "message": "Page does not exist",
        "locations": [{
            "line": 3,
            "column": 5
        }],
        "path": ["analyticsForMeetingsDurations"]
    }],
    "data": {
        "analyticsForMeetingsDurations": null
    }
}

get_weekly_meetings_total_duration_no_meetings_query = '''
query {
    analyticsForMeetingsDurations(startDate:"Aug 12 2018", endDate:"Aug 12 2018"){  # noqa: E501
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

get_weekly_meetings_total_duration_no_meetings_response = {
    'data': {
        'analyticsForMeetingsDurations': {
            'MeetingsDurationaAnalytics': []
        }
    }
}
