query_events = '''
    query{
        allEvents(startDate: "Jul 9 2018", endDate: "Jul 20 2018"){
            id
            room{
                name
            }
            eventTitle
        }
    }
'''
event_query_response = {
    'data': {
        'allEvents':
        [{
            'id': '1',
            'room': {
                'name': 'Entebbe'
                },
            'eventTitle': 'Onboarding'
        }]
    }
}
