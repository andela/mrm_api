null = None
true = True
false = False

get_daily_meetings_total_duration_query = '''
query {
    analyticsForMeetingsDurations(startDate:"Jul 11 2018"){
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
                    "count": 1,
                    "totalDuration": 45,
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
    analyticsForMeetingsDurations(startDate:"Jul 11 2018", endDate:"Jul 11 2018"){  # noqa: E501
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
                    'count': 1,
                    'totalDuration': 45,
                    "events": [
                        {
                            "durationInMinutes": 45,
                            "numberOfMeetings": 1
                        }
                    ]
                    }]}}}

get_paginated_meetings_total_duration_query = '''
query {
    analyticsForMeetingsDurations(startDate:"Jul 11 2018", perPage:1, page:1){
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
          "count": 1,
          "totalDuration": 45,
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

get_paginated_meetings_total_duration_query_invalid_page = '''
query {
    analyticsForMeetingsDurations(startDate:"Jul 11 2018", perPage:1, page:100){
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
