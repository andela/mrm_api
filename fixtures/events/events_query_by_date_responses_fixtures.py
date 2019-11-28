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
