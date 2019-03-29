daily_room_events_query = '''
query{
    analyticsForDailyRoomEvents(startDate:"Jul 11 2018", endDate:"Jul 11 2018"){
        DailyRoomEvents {
            day
            events{
                eventSummary
                startTime
                endTime
                roomName
                noOfParticipants
            }
        }
    }
}
'''
daily_room_events_wrong_date_format_query = '''
query{
    analyticsForDailyRoomEvents(startDate:"10 jan 2019", endDate:"jan 10 2019"){
        DailyRoomEvents {
            day
            events {
                noOfParticipants,
                eventSummary,
                startTime,
                endTime,
                roomName,
                eventId
            }
        }
    }
}
'''

daily_room_events_response = {
  "data": {
    "analyticsForDailyRoomEvents": {
      "DailyRoomEvents": [
        {
            "day": "Wed Jul 11 2018",
            "events": [
                {
                    'endTime': '09:45:00',
                    'eventSummary': 'Onboarding',
                    'noOfParticipants': 4,
                    'roomName': 'Entebbe',
                    'startTime': '09:00:00'
                }
            ]
        }
      ]
    }
  }
}

paginated_daily_room_events_query = '''
query{
    analyticsForDailyRoomEvents(startDate:"Jul 11 2018",page:1, perPage:1,
     endDate:"Jul 11 2018"){
        DailyRoomEvents {
            day
            events{
                eventSummary
                startTime
                endTime
                roomName
                noOfParticipants
            }
        }
        pages
        hasNext
        hasPrevious
    }
}'''

invalid_page_for_analytics_for_daily_events_query = '''
query{
    analyticsForDailyRoomEvents(startDate:"Jul 11 2018",page:1500, perPage:1000,
     endDate:"Jul 11 2018"){
        DailyRoomEvents {
            day
            events{
                eventSummary
                startTime
                endTime
                roomName
                noOfParticipants
            }
        }
        pages
        hasNext
        hasPrevious
    }
}'''  # fetch for invalid page number(non-existing)


daily_paginated_room_events_response = {
  "data": {
    "analyticsForDailyRoomEvents": {
      "DailyRoomEvents": [
        {
          "day": "Wed Jul 11 2018",
          "events": [
            {
              "eventSummary": "Onboarding",
              "startTime": "09:00:00",
              "endTime": "09:45:00",
              "roomName": "Entebbe",
              "noOfParticipants": 4
            }
          ]
        }
      ],
      "pages": 1,
      "hasNext": False,
      "hasPrevious": False
    }
  }
}

daily_events_wrong_date_format_response = {'errors': [
    {
        'message': "time data '10 jan 2019' does not match format '%b %d %Y'",
        'locations': [{'line': 3, 'column': 5}],
        'path': ['analyticsForDailyRoomEvents']}],
    'data': {
        'analyticsForDailyRoomEvents': None
}
}
