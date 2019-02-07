null = None

room_response_query_sample = '''{
    roomResponse(roomId:1) {
        roomName,
        totalResponses,
        response{
            responseId,
            createdDate,
            missingItems,
            suggestion,
            rating
        }
    }
}
'''

get_room_response_query = '''{
    roomResponse(roomId:1) {
        roomName,
        totalResponses
    }
}
'''

get_room_response_query_data = {
    "data": {
        "roomResponse": {
            "roomName": "Entebbe",
            "totalResponses": 2
        }
    }
}

get_room_response_non_existence_room_id = '''{
    roomResponse(roomId:15) {
        roomName,
        totalResponses,
        response{
            responseId,
            missingItems,
            suggestion,
            rating
        }
    }
}
'''

summary_room_response_query = '''{
    allRoomResponses {
        responses {
        roomName,
        totalResponses,
        response {
          responseId,
          rating,
          suggestion,
          missingItems
        }
      }
    }
}
'''

summary_room_response_data = {
    "data": {
        "allRoomResponses": {
            "responses": [
                {
                    "roomName": "Entebbe",
                    "totalResponses": 2,
                    "response": [
                        {
                            "responseId": 2,
                            "rating": None,
                            "suggestion": None,
                            "missingItems": ['Markers']
                        },
                        {
                            "responseId": 1,
                            "rating": 2,
                            "suggestion": None,
                            "missingItems": []
                        }
                    ]
                }
            ]
        }
    }
}

filter_by_response_query = '''
query{
    allRoomResponses(upperLimit: 2, lowerLimit: 0 ){
        responses{
            totalResponses
            roomName
            response{
                responseId
                missingItems
            }
        }
    }
}
'''

filter_by_response_invalid_query = '''
query{
    allRoomResponses(upperLimit: 2){
        responses{
            totalResponses
            roomName
            response{
                responseId
                missingItems
            }
        }
    }
}
'''

search_response_by_room_query = '''
query{
    allRoomResponses(upperLimit: 2, lowerLimit: 0, room:"Entebbe"){
        responses{
            totalResponses
            roomName
            response{
                responseId
                missingItems
            }
        }
    }
}
'''

search_response_by_room_beyond_limits_query = '''
query{
    allRoomResponses(upperLimit: 7, lowerLimit: 5, room:"Entebbe"){
        responses{
            totalResponses
            roomName
            response{
                responseId
                missingItems
            }
        }
    }
}
'''

search_response_by_room_invalid_room_query = '''
query{
    allRoomResponses(upperLimit: 2, lowerLimit: 0, room:"Entebbes"){
        responses{
            totalResponses
            roomName
            response{
                responseId
                missingItems
            }
        }
    }
}
'''

search_response_by_room_only = '''
query{
    allRoomResponses(room:"Entebbe"){
        responses{
            totalResponses
            roomName
            response{
                responseId
                missingItems
            }
        }
    }
}
'''

search_response_by_invalid_room = '''
query{
    allRoomResponses(room:"Entebbes"){
        responses{
            totalResponses
            roomName
            response{
                responseId
                missingItems
            }
        }
    }
}
'''

search_response_by_room_no_response = '''
query{
    allRoomResponses(room:"Kampala"){
        responses{
            totalResponses
            roomId
            roomName
            response{
                responseId
                missingItems
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
                            'missingItems': ['Markers'],
                            'responseId': 2,
                        },
                        {
                            'missingItems': [],
                            'responseId': 1,
                        }

                    ],
                    'roomName': 'Entebbe',
                    'totalResponses': 2,
                }
            ]
        }
    }
}
