null = None

create_rate_query = '''
mutation{
  createResponse(responses: [{questionId:1, rate:2}], roomId:1) {
    response{
      id
      questionId
      roomId
      rate
      }
  }
}
'''

create_rate_response = {
  "data": {
    "createResponse": {
      "response": [
        {
          "id": "3",
          "questionId": 1,
          "roomId": 1,
          "rate": 2
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
      rate
      }
  }
}
'''

rate_non_existing_question_response = {
  "errors": [
    {
      "message": "Question does not exist",
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

invalid_rating_number = '''
mutation{
  createResponse(responses: [{questionId:1, rate:6}], roomId:1) {
    response{
      id
      questionId
      roomId
      rate
      }
  }
}
'''

invalid_rating_number_response = {
  "errors": [
    {
      "message": "Please rate between 1 and 5",
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

rate_with_non_existent_room = '''
mutation{
  createResponse(responses: [{questionId:1, rate:2}], roomId:9) {
    response{
      id
      questionId
      roomId
      rate
      }
  }
}
'''

rate_with_non_existent_room_response = {
  "errors": [
    {
      "message": "Non-existent room id",
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

response_for_database_error = {
    "errors": [
        {
            "message": "There seems to be a database connection error, \
                contact your administrator for assistance",
            "locations": [
                {

                    "line": 3,
                    "column": 3
                }
                ],
            "path": [
                "createResponse"
            ]
        }
    ],
    "data": {"createResponse": null}}

response_for_update_response_with_database_error = {
    "errors": [
        {
            "message": "There seems to be a database connection error, \
                contact your administrator for assistance",
            "locations": [
                {

                    "line": 3,
                    "column": 3
                }
                ],
            "path": [
                "updateResponse"
            ]
        }
    ],
    "data": {"updateResponse": null}}

responce_for_creating_response_with_database_error = {
    "errors": [
        {
            "message": "Cannot return null for non-nullable field Response.id.",
            "locations": [
                {
                    "line": 5,
                    "column": 7
                }
             ],
            "path": ['createResponse', 'response', 0, 'id']
        }
    ],
    "data": {'createResponse': {'response': [None]}},
    }
