import datetime

null = None

start_date = (datetime.date.today() - datetime.timedelta(
    days=2)).strftime('%b %d %Y')
end_date = datetime.date.today().strftime('%b %d %Y')
invalid_start_date = (datetime.date.today() + datetime.timedelta(
    days=10)).strftime('%b %d %Y')
invalid_end_date = (datetime.date.today() + datetime.timedelta(
    days=20)).strftime('%b %d %Y')

room_response_query_sample = '''{
    roomResponse(roomId:1) {
        roomName,
        totalResponses,
        response{
            responseId,
            createdDate,
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

get_resolved_room_responses_query = '''{
    roomResponse(roomId:1, resolved:true) {
        roomName,
        totalResponses
    }
}
'''

get_resolved_room_responses_query_data = {
    "data": {
        "roomResponse": {
            "roomName": "Entebbe",
            "totalResponses": 1
        }
    }
}

get_room_response_query_by_date = '''
query{{
    allRoomResponses(startDate: "{}",
     endDate: "{}" ){{
        responses{{
            totalResponses
            roomName
            response{{
                responseId
                response{{
                  ... on Rate{{
                    rate
                  }}
                  ... on SelectedOptions{{
                    options
                  }}
                  ... on TextArea{{
                    suggestion
                  }}
                  ... on MissingItems{{
                    missingItems{{
                      name
                    }}
                  }}
                  }}
            }}
        }}
    }}
}}
'''.format(start_date, end_date)

get_room_response_query_by_date_and_limits = '''
query{{
    allRoomResponses(startDate: "{}",
     endDate: "{}",
     upperLimitCount: 3, lowerLimitCount: 0,
     room:"Entebbe" ){{
        responses{{
            totalResponses
            roomName
            response{{
                responseId
                response{{
                  ... on Rate{{
                    rate
                  }}
                  ... on SelectedOptions{{
                    options
                  }}
                  ... on TextArea{{
                    suggestion
                  }}
                  ... on MissingItems{{
                    missingItems{{
                      name
                    }}
                  }}
                  }}
            }}
        }}
    }}
}}
'''.format(start_date, end_date)

get_room_response_query_with_invalid_date = '''
query{{
    allRoomResponses(startDate: "{}",
     endDate: "{}" ){{
        responses{{
            totalResponses
            roomName
            response{{
                responseId
                response{{
                  ... on Rate{{
                    rate
                  }}
                  ... on SelectedOptions{{
                    options
                  }}
                  ... on TextArea{{
                    suggestion
                  }}
                  ... on MissingItems{{
                    missingItems{{
                      name
                    }}
                  }}
                  }}
            }}
        }}
    }}
}}
'''.format(invalid_start_date, invalid_end_date)

get_room_response_query_with_higher_start_date = '''
query{{
    allRoomResponses(startDate: "{}",
     endDate: "{}" ){{
        responses{{
            totalResponses
            roomName
            response{{
                responseId
                response{{
                  ... on Rate{{
                    rate
                  }}
                  ... on SelectedOptions{{
                    options
                  }}
                  ... on TextArea{{
                    suggestion
                  }}
                  ... on MissingItems{{
                    missingItems{{
                      name
                    }}
                  }}
                  }}
            }}
        }}
    }}
}}
'''.format(end_date, start_date)

get_room_response_query_by_date_data = {
  "data": {
    "allRoomResponses": {
      "responses": [
        {
          "totalResponses": 2,
          "roomName": "Entebbe",
          "response": [
            {
              "responseId": 2,
              "response": {
                "options": [
                  "marker pen",
                  "apple tv"
                ]
              }
            },
            {
              "responseId": 1,
              "response": {
                "rate": 1
              }
            }
          ]
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
            response{
          ... on Rate{
            rate
          }
          ... on TextArea{
            suggestion
          }
          ... on SelectedOptions{
            options
          }
          ... on MissingItems{
            missingItems{
              name
            }
          }
        }
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
          response {
            ... on Rate{
              rate
            }
            ... on SelectedOptions{
              options
            }
            ... on TextArea{
              suggestion
            }
            ... on MissingItems{
              missingItems{
                name
                id
              }
            }
          }
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
              "response": {
                "options": [
                  "marker pen",
                  "apple tv"
                ]
              }
            },
            {
              "responseId": 1,
              "response": {
                "rate": 1
              }
            }
          ]
        }
      ]
    }
  }
}

all_resolved_room_response_query = '''{
    allRoomResponses(resolved:true) {
        responses {
        roomName,
        totalResponses,
        response {
          responseId,
          response {
            ... on Rate{
              rate
            }
            ... on SelectedOptions{
              options
            }
            ... on TextArea{
              suggestion
            }
            ... on MissingItems{
              missingItems{
                name
                id
              }
            }
          }
        }
      }
    }
}
'''

all_resolved_room_response_data = {
  "data": {
    "allRoomResponses": {
      "responses": [
        {
          "roomName": "Entebbe",
          "totalResponses": 1,
          "response": [
            {
              "responseId": 2,
              "response": {
                "options": [
                  "marker pen",
                  "apple tv"
                ]
              }
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
                            'responseId': 2,
                        },
                        {
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

search_resolved_responses_by_room_name = '''
query{
    allRoomResponses(room:"Entebbe", resolved:true){
        responses{
            totalResponses
            roomName
            response{
                responseId
                response {
                  ... on Rate{
                    rate
                  }
                  ... on SelectedOptions{
                    options
                  }
                  ... on TextArea{
                    suggestion
                  }
                  ... on MissingItems{
                    missingItems{
                      name
                      id
                    }
                  }
                }
            }
        }
    }
}
'''

search_resolved_responses_by_room_name_data = {
  "data": {
    "allRoomResponses": {
      "responses": [
        {
          "roomName": "Entebbe",
          "totalResponses": 1,
          "response": [
            {
              "responseId": 2,
              "response": {
                "options": [
                  "marker pen",
                  "apple tv"
                ]
              }
            }
          ]
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
          response {
            ... on Rate{
              rate
            }
            ... on SelectedOptions{
              options
            }
            ... on TextArea{
              suggestion
            }
            ... on MissingItems{
              missingItems{
                name
              }
            }
          }
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
              "response": {
                "options": [
                  "marker pen",
                  "apple tv"
                ]
              }
            },
            {
              "responseId": 1,
              "response": {
                "rate": 1
              }
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
          response{
            ... on Rate{
              rate
            }
            ... on TextArea{
              suggestion
            }
            ... on SelectedOptions{
              options
            }
            ... on MissingItems{
              missingItems{
                name
              }
            }
          }
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
      response{
        ... on Rate{
          rate
        }
        ... on TextArea{
          suggestion
        }
        ... on SelectedOptions{
          options
        }
        ... on MissingItems{
          missingItems{
            name
          }
        }
      }
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
        "id": 1,
        "response": {
          "rate": 1
        },
        "roomId": 1
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
        response{
          ... on Rate{
            rate
          }
          ... on TextArea{
            suggestion
          }
          ... on SelectedOptions{
            options
          }
          ... on MissingItems{
            missingItems{
              name
            }
          }
        }
      roomId
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
                "id": 2,
                "roomId": 1,
            }
        }
    }
}

mark_multiple_as_resolved_mutation = '''
    mutation{
  resolveMultipleResponses(responses:[1], resolved:true){
    handledResponses{
      responses{
        id
        resolved
        response{
          ... on Rate{
            rate
          }
          ... on TextArea{
            suggestion
          }
          ... on SelectedOptions{
            options
          }
          ... on MissingItems{
            missingItems{
              name
            }
        }
        }
      }
      totalResponses
    }
  }
}
'''

mark_multiple_as_resolved_response = {
  "data": {
    "resolveMultipleResponses": {
      "handledResponses": {
        "responses": [
          {
            "id": 1,
            "resolved": True,
            "response": {
              "rate": 1
            }
          }
        ],
        "totalResponses": 1
      }
    }
  }
}

mark_multiple_as_unresolved_mutation = '''
    mutation{
  resolveMultipleResponses(responses:[1], resolved:false){
    handledResponses{
      responses{
        id
        resolved
        response{
          ... on Rate{
            rate
          }
          ... on TextArea{
            suggestion
          }
          ... on SelectedOptions{
            options
          }
          ... on MissingItems{
            missingItems{
              name
            }
        }
        }
      }
      totalResponses
    }
  }
}
'''

mark_multiple_as_unresolved_response = {
  "data": {
    "resolveMultipleResponses": {
      "handledResponses": {
        "responses": [
          {
            "id": 1,
            "resolved": False,
            "response": {
              "rate": 1
            }
          }
        ],
        "totalResponses": 1
      }
    }
  }
}

mark_multiple_as_resolved_with_invalid_id = '''
    mutation{
  resolveMultipleResponses(responses:[36], resolved:true){
    handledResponses{
      responses{
        id
        resolved
        response{
          ... on TextArea{
          suggestion
        }
        }
      }
      totalResponses
    }
  }
}
'''
