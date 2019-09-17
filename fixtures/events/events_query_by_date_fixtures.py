query_events = '''
    query{
        allEvents(startDate: "Jul 9 2018", endDate: "Jul 9 2018"){
            events {
                eventTitle
            }
        }
    }
'''
event_query_response = {
  "errors": [
    {
      "message": "Events do not exist for the date range",
      "locations": [
        {
          "line": 3,
          "column": 9
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

query_events_with_start_date_before_end_date = '''
    query{
        allEvents(startDate: "Jul 20 2018",
                  endDate: "Jul 09 2018",
                  page:1,
                  perPage: 2){
            events {
                eventTitle

            },
            hasNext,
            hasPrevious,
            pages,
            queryTotal
        }
    }
'''

event_query_with_start_date_before_end_date_response = {
    "errors": [
      {
        "message": "Start date must be lower than end date",
        "locations": [
          {
            "line": 3,
            "column": 9
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

query_events_with_pagination = '''
    query{
        allEvents(startDate: "Jul 11 2018",
                  endDate: "Jul 11 2018",
                  page:1,
                  perPage: 1){
            events {
                    id
                    roomId
                    room{
                        name
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
            'events': [{
                    'id': '1',
                    'roomId': 1,
                    'room': {
                        'name': 'Entebbe'
                        }
            }],
            'hasNext': False,
            'hasPrevious': False,
            'pages': 1,
            'queryTotal': 1
        }
    }
}

query_events_with_location = '''
    query{
        allEvents(startDate: "Jul 11 2018",
                  endDate: "Jul 11 2018",
                  page:1,
                  perPage: 1){
            events {
                    id
                    roomId
                    room{
                        name
                        locationId
                    }
            },
            hasNext,
            hasPrevious,
            pages,
            queryTotal
        }
    }
'''

event_query_with_location_response = {
    'data': {
        'allEvents': {
            'events': [{
                    'id': '1',
                    'roomId': 1,
                    'room': {
                        'name': 'Entebbe',
                        'locationId': 1
                        }
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
  allEvents(
      startDate: "Mar 28 2019",
      endDate: "Mar 29 2019",
      page: 1
    ){
    events {
      eventTitle
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
  allEvents(
      startDate: "Mar 28 2019",
      endDate: "Mar 29 2019",
      perPage: 1
    ){
    events {
      eventTitle
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
    events {
      eventTitle
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
    events {
      eventTitle
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

query_events_without_start_date = '''
  query{
    allEvents(
        endDate: "Mar 29 2019",
        perPage: 1,
        page: 3
      ){
      events {
        eventTitle
      }
      hasNext
      hasPrevious
      pages
      queryTotal

    }
  }
'''

event_query_without_start_date_response = {
  "errors": [
    {
      "message": "startDate argument missing",
      "locations": [
        {
          "line": 3,
          "column": 5
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

query_events_without_end_date = '''
  query{
    allEvents(
        startDate: "Mar 29 2019",
        perPage: 1,
        page: 3
      ){
      events {
        eventTitle
      }
      hasNext
      hasPrevious
      pages
      queryTotal

    }
  }
'''

event_query_without_end_date_response = {
  "errors": [
    {
      "message": "endDate argument missing",
      "locations": [
        {
          "line": 3,
          "column": 5
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

query_events_without_page_and_per_page = '''
query{
  allEvents(startDate: "Jul 11 2018",
            endDate: "Jul 11 2018"){
        events {
                id
                roomId
                room{
                    name
                }
        },
        hasNext,
        hasPrevious,
        pages,
        queryTotal
    }
  }
'''

event_query_without_page_and_per_page_response = {
  'data': {
        'allEvents': {
            'events': [{
                    'id': '1',
                    'roomId': 1,
                    'room': {
                        'name': 'Entebbe'
                        }
            }],
            'hasNext': None,
            'hasPrevious': None,
            'pages': None,
            'queryTotal': None
        }
    }
}

query_events_without_start_and_end_date = '''
  query{
      allEvents(perPage: 1, page: 3){
          events {
              eventTitle
          }
      }
  }
'''

event_query_without_start_and_end_date_response = {

  "errors": [
    {
      "message": "Page does not exist",
      "locations": [
        {
          "line": 3,
          "column": 7
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
