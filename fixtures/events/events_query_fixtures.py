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
