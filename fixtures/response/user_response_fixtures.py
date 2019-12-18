from ..output.OutputBuilder import build
from ..output.Error import error_item

null = None

create_rate_query = '''
mutation{
  createResponse(responses: [{questionId:1, rate:2}], roomId:1) {
    response{
      id
      questionId
      roomId
      response{
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
}
'''

create_rate_response = {
  "data": {
    "createResponse": {
      "response": [
        {
          "id": "4",
          "questionId": 1,
          "roomId": 1,
          "response": {
            "rate": 2
          }
        }
      ]
    }
  }
}

rate_non_existing_question = '''
mutation{
  createResponse(questionId:5, roomId:1, rate:2) {
    response{
      id
      questionId
      roomId
      response
      }
  }
}
'''

rne_error = error_item
rne_error.message = "Question does not exist"
rne_error.locations = [{"line": 2, "column": 3}]
rne_error.path = ["createResponse"]
rne_data = {"createResponse": null}
rate_non_existing_question_response = build(
    error=rne_error.build_error(rne_error),
    data=rne_data
)

invalid_rating_number = '''
mutation{
  createResponse(responses: [{questionId:1, rate:6}], roomId:1) {
    response{
      id
      questionId
      roomId
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
'''

irn_error = error_item
irn_error.message = "Please rate between 1 and 5"
irn_error.locations = [{"line": 2, "column": 3}]
irn_error.path = ["createResponse"]
irn_data = {"createResponse": null}
invalid_rating_number_response = build(
    error=irn_error.build_error(irn_error),
    data=irn_data
)

rate_with_non_existent_room = '''
mutation{
  createResponse(responses: [{questionId:1, rate:2}], roomId:9) {
    response{
      id
      questionId
      roomId
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
'''

rwn_error = error_item
rwn_error.message = "Non-existent room id"
rwn_error.locations = [{"line": 2, "column": 3}]
rwn_error.path = ["createResponse"]
rwn_data = {"createResponse": null}
rate_with_non_existent_room_response = build(
    error=rwn_error.build_error(rwn_error),
    data=rwn_data
)
