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

query_paginated_responses = '''
    query{
  allRoomResponses(page:1, perPage:2){
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
   hasNext
   hasPrevious
   pages
}
}
'''

query_paginated_responses_response = {
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
            ],
            "hasNext": False,
            "hasPrevious": False,
            "pages": 1
        }
    }
}

query_paginated_responses_empty_page = '''
    query{
  allRoomResponses(page:5, perPage:2){
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
   hasNext
   hasPrevious
   pages
}
}
'''

mark_response_as_resolved_mutation = '''
    mutation{
  resolveRoomResponse(responseId:1){
    roomResponse{
      resolved
      id
      rate
      roomId
    }
  }
}
'''

mark_user_response_as_resolved_mutation_response = {
  "data": {
    "resolveRoomResponse": {
      "roomResponse": {
        "resolved": True,
        "id": "1",
        "rate": 2,
        "roomId": 1,
      }
    }
  }
}
mark_response_as_resolved_mutation_with_an_invalid_response_id = '''
    mutation{
    resolveRoomResponse(responseId:4){
        roomResponse{
        resolved
        id
        rate
        roomId
        textArea
        }
    }
}
'''

mark_a_user_response_as_unresolved_mutation = '''
    mutation{
  resolveRoomResponse(responseId:2){
    roomResponse{
      resolved
      id
      roomId
    }
  }
}
'''

mark_a_user_response_as_unresolved_mutation_response = {
  "data": {
    "resolveRoomResponse": {
      "roomResponse": {
        "resolved": False,
        "id": "2",
        "roomId": 1,
      }
    }
  }
}
