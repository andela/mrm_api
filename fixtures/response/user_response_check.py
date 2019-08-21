null = None

check_non_existing_question = '''
mutation{
  createResponse(responses: [{questionId:5, missingItems:[1]}], roomId:1) {
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

check_non_existing_question_response = {
    "errors": [
        {
            "message": "Response to question",
            "locations": [
                {
                    "line": 2,
                    "column": 3
                }
            ],
            "path": [
                "createResponse"
            ]
        }
    ],
    "data": {
        "createResponse": null
    }
}

check_with_non_existent_room = '''
mutation{
  createResponse(responses: [{questionId:2,  missingItems:[1]}], roomId:9) {
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

create_check_query = '''
mutation{
  createResponse(responses: [{questionId:2, missingItems:[1]}], roomId:1) {
    response{
      id
      questionId
      roomId
      }
  }
}
'''

create_check_response = {
    "data": {
        "createResponse": {
            "response": [
                {
                    "id": "3",
                    "questionId": 2,
                    "roomId": 1
                }
            ]
        }
    }
}

filter_question_by_room = '''
{
  getRoomResponse(roomId: 1, perPage: 1, page: 1) {
    responses {
      roomName
      roomId
      response {
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
                id
              }
            }
          }
      }
    }
  }
}
'''

filter_question_by_room_response = {
  "data": {
    "getRoomResponse": {
      "responses": [
        {
          "roomName": "Entebbe Test",
          "roomId": 1,
          "response": [
            {
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

filter_response_by_room_with_pagination = '''
{
  getRoomResponse(roomId: 1, perPage: 1, page: 1) {
    responses {
      roomName
      roomId
      response {
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
                id
              }
            }
          }
      }
    }
  }
}
'''

filter_response_by_room_with_pagination_response = {
  "data": {
    "getRoomResponse": {
      "responses": [
        {
          "roomName": "Entebbe Test",
          "roomId": 1,
          "response": [
            {
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

filter_question_by_invalid_room = '''
{
  getRoomResponse(roomId: 100, perPage: 1, page: 1) {
    responses {
      roomName
      roomId
      response {
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
                id
              }
            }
          }
      }
    }
  }
}

'''

filter_question_by_invalid_room_response = {
    "errors": [{
        "message": "This room doesn't exist or doesn't have feedback.",
        "locations": [{
            "line": 3,
            "column": 3
        }],
        "path": ["getRoomResponse"]
    }],
    "data": {
        "getRoomResponse": null
    }
}
