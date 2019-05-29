query_events = '''
    query{
        allEvents(startDate: "Jul 9 2018", endDate: "Jul 20 2018"){
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
'''
event_query_response = {
    'data': {
        'allEvents': [{
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
