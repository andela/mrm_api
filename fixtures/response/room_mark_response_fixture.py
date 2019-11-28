from ..output.OutputBuilder import build

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

user_response_data_resolved = {
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

mark_user_response_as_resolved_mutation_response = build(
    data=user_response_data_resolved
)

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

mark_multiple_response_data = {
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
mark_multiple_as_resolved_response = build(
    data=mark_multiple_response_data
)

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
