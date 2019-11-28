from ..output.OutputBuilder import build
from ..output.Error import error_item

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
aur_error = error_item
aur_error.message = "The specified response does not exist or hasn't been resolved yet."  # noqa: E501
aur_error.locations = [{"line": 3, "column": 3}]
aur_error.path = ["archiveResolvedResponse"]
aur_data = {"archiveResolvedResponse": null}
archive_unresolved_response_response = build(
    error=aur_error.build_error(aur_error),
    data=aur_data
)

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
ane_error = error_item
ane_error.message = "The specified response does not exist or hasn't been resolved yet."  # noqa: E501
ane_error.locations = [{"line": 3, "column": 3}]
ane_error.path = ["archiveResolvedResponse"]
ane_data = {"archiveResolvedResponse": null}
archive_non_existing_response_response = build(
    error=ane_error.build_error(ane_error),
    data=ane_data
)

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
                    "roomName": "Tana",
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
