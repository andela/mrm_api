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

get_room_response_query_response = {
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
    allRoomResponses(filterBy:"Responses",upperLimit: 2, lowerLimit: 0 ){
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

filter_by_response_data = {
    'data': {
        'allRoomResponses': {
            'responses': [
                {
                    'totalResponses': 2,
                    'roomName': 'Entebbe',
                    'response': [
                        {
                            'responseId': 2,
                            'missingItems': ['Markers'],
                        },
                        {
                            'responseId': 1,
                            'missingItems': [],
                        }

                    ]
                }
            ]
        }
    }
}
