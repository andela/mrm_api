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

get_room_response_query_by_date = '''
query{
    allRoomResponses(lowerDateLimit: "2019 feb 20",
     upperDateLimit: "2019 feb 25" ){
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
get_room_response_query_with_invalid_date = '''
query{
    allRoomResponses(lowerDateLimit: "2019 feb 20",
     upperDateLimit: "2019 Mar 25" ){
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
get_room_response_query_with_higher_lower_limit = '''
query{
    allRoomResponses(lowerDateLimit: "2019 feb 20",
     upperDateLimit: "2019 feb 1" ){
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

get_room_response_query_by_date_query = {
  "data": {
    "allRoomResponses": {
      "responses": [
        {
          "totalResponses": 2,
          "roomName": "Entebbe",
          "response": []
        }
      ]
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
    allRoomResponses(upperLimitCount: 3, lowerLimitCount: 0 ){
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
    allRoomResponses(upperLimitCount: 2){
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
    allRoomResponses(lowerLimitCount: 1, upperLimitCount: 3, room:"Entebbe"){
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
    allRoomResponses(upperLimitCount: 7, lowerLimitCount: 5, room:"Entebbe"){
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
    allRoomResponses(upperLimitCount: 2, lowerLimitCount: 0, room:"Entebbes"){
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
    allRoomResponses(room:"Mubende"){
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
