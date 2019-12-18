filter_by_response_query = '''
query{
    allRoomResponses(upperLimitCount: 3, lowerLimitCount: 0 ){
        responses{
            totalResponses
            roomName
            response{
                id
            }
        }
    }
}
'''

filter_by_response_invalid_query = '''
query{
    allRoomResponses(upperLimitCount: 2){
        responses{
            totalResponses
            roomName
            response{
                id
            }
        }
    }
}
'''

filter_by_response_data = {
    'data': {
        'allRoomResponses': {
            'responses': [
                {
                    'response': [
                        {
                            'id': 2,
                        },
                        {
                            'id': 1,
                        }

                    ],
                    'roomName': 'Entebbe',
                    'totalResponses': 2,
                }
            ]
        }
    }
}
