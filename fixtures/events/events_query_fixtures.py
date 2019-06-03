query_events = '''
    query{
        allEvents(startDate: "Jul 9 2018", endDate: "Jul 20 2018"){
            DailyRoomEvents {
                day
                events{
                    id
                    roomId
                    room{
                        name
                    }
                }
            }
        }
    }
'''
event_query_response = {
    'data': {
        'allEvents': {
            'DailyRoomEvents': [{
                'day': 'Wed Jul 11 2018',
                'events': [{
                    'id': '1',
                    'roomId': 1,
                    'room': {
                        'name': 'Entebbe'
                        }
                    }]
            }]
        }
    }
}

query_events_with_pagination = '''
    query{
        allEvents(startDate: "Jul 9 2018",
                  endDate: "Jul 20 2018",
                  page:1,
                  perPage: 2){
            DailyRoomEvents {
                day
                events{
                    id
                    roomId
                    room{
                        name
                    }
                }
            },
            hasNext,
            hasPrevious,
            pages,
            queryTotal
        }
    }
'''

event_query_with_pagination_response = {
    'data': {
        'allEvents': {
            'DailyRoomEvents': [{
                'day': 'Wed Jul 11 2018',
                'events': [{
                    'id': '1',
                    'roomId': 1,
                    'room': {
                        'name': 'Entebbe'
                        }
                    }]
            }],
            'hasNext': False,
            'hasPrevious': False,
            'pages': 1,
            'queryTotal': 1
        }
    }
}

query_events_page_without_per_page = '''
query{
  allEvents(startDate: "Mar 28 2019", endDate: "Mar 29 2019", page: 1){
    DailyRoomEvents {
      day
      events {
        eventTitle
      }
    }
    hasNext
    hasPrevious
    pages
    queryTotal

  }
}
'''

event_query_page_without_per_page_response = {
  "errors": [
    {
      "message": "perPage argument missing",
      "locations": [
        {
          "line": 3,
          "column": 3
        }
      ],
      "path": [
        "allEvents"
      ]
    }
  ],
  "data": {
    "allEvents": None
  }
}

query_events_per_page_without_page = '''
query{
  allEvents(startDate: "Mar 28 2019", endDate: "Mar 29 2019", perPage: 1){
    DailyRoomEvents {
      day
      events {
        eventTitle
      }
    }
    hasNext
    hasPrevious
    pages
    queryTotal

  }
}
'''

event_query_perPage_without_page_response = {
  "errors": [
    {
      "message": "page argument missing",
      "locations": [
        {
          "line": 3,
          "column": 3
        }
      ],
      "path": [
        "allEvents"
      ]
    }
  ],
  "data": {
    "allEvents": None
  }
}


query_events_invalid_page = '''
query{
  allEvents(
      startDate: "Mar 28 2019",
      endDate: "Mar 29 2019",
      page: 0,
      perPage:1
      ){
    DailyRoomEvents {
      day
      events {
        eventTitle
      }
    }
    hasNext
    hasPrevious
    pages
    queryTotal

  }
}
'''

event_query_invalid_page_response = {
  "errors": [
    {
      "message": "page must be at least 1",
      "locations": [
        {
          "line": 3,
          "column": 3
        }
      ],
      "path": [
        "allEvents"
      ]
    }
  ],
  "data": {
    "allEvents": None
  }
}

query_events_invalid_per_page = '''
query{
  allEvents(
      startDate: "Mar 28 2019",
      endDate: "Mar 29 2019",
      page: 1,
      perPage:0
      ){
    DailyRoomEvents {
      day
      events {
        eventTitle
      }
    }
    hasNext
    hasPrevious
    pages
    queryTotal

  }
}
'''

event_query_invalid_per_page_response = {
  "errors": [
    {
      "message": "perPage must be at least 1",
      "locations": [
        {
          "line": 3,
          "column": 3
        }
      ],
      "path": [
        "allEvents"
      ]
    }
  ],
  "data": {
    "allEvents": None
  }
}
