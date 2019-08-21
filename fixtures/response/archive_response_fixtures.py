null = None
true = True

archive_response_mutation = '''
mutation{
  archiveResolvedResponse(responseId:2){
    roomResponse{
      id
      roomId
      questionType
      resolved
    }
  }
}
'''

archive_response_response = {
    "data": {
        "archiveResolvedResponse": {
            "roomResponse": {
                "id": 2,
                "roomId": 1,
                "questionType": "check",
                "resolved": true
            }
        }
    }
}

archive_unresolved_response_mutation = '''
mutation{
  archiveResolvedResponse(responseId:1){
    roomResponse{
      id
      roomId
      questionType
      resolved
    }
  }
}
'''

archive_unresolved_response_response = {
    "errors": [
        {
            "message": "The specified response does not exist or hasn't been resolved yet.",  # noqa: E501
            "locations": [
                {
                    "line": 3,
                    "column": 3
                }
            ],
            "path": [
                "archiveResolvedResponse"
            ]
        }
    ],
    "data": {
        "archiveResolvedResponse": null
    }
}

archive_non_existing_response_mutation = '''
mutation{
  archiveResolvedResponse(responseId:14){
    roomResponse{
      id
      roomId
      questionType
      resolved
    }
  }
}
'''

archive_non_existing_response_response = {
    "errors": [
        {
            "message": "The specified response does not exist or hasn't been resolved yet.",  # noqa: E501
            "locations": [
                {
                    "line": 3,
                    "column": 3
                }
            ],
            "path": [
                "archiveResolvedResponse"
            ]
        }
    ],
    "data": {
        "archiveResolvedResponse": null
    }
}

filter_archived_responses_query = '''
{
  allRoomResponses(page:1, perPage:1, archived:true) {
    responses {
      roomId
      roomName
      response {
        id
        state
        response {
          ... on Rate {
            rate
          }
          ... on SelectedOptions {
            options
          }
          ... on TextArea {
            suggestion
          }
          ... on MissingItems {
            missingItems {
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

filter_archived_responses_response = {
    "data": {
        "allRoomResponses": {
            "responses": [
                {
                    "roomId": 2,
                    "roomName": "Tana Dummy",
                    "response": [
                        {
                            "id": 3,
                            "state": "archived",
                            "response": {
                                "options": [
                                    "duster"
                                ]
                            }
                        }
                    ]
                }
            ]
        }
    }
}
