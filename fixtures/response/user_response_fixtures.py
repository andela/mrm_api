null = None

create_rate_query = '''
mutation{
  createResponse(questionId:1, roomId:1, rate:2) {
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
      "response": {
        "id": "2",
        "questionId": 1,
        "roomId": 1,
        "rate": 2
      }
    }
  }
}

rate_wrong_question = '''
mutation{
  createResponse(questionId:2, roomId:1, rate:2) {
    response{
      id
      questionId
      roomId
      rate
      }
  }
}
'''

rate_wrong_question_response = {
  "errors": [
    {
      "message": "Provide a rating response",
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

rate_non_existing_question = '''
mutation{
  createResponse(questionId:5, roomId:1, rate:2) {
    response{
      id
      questionId
      roomId
      rate
      userId
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
  createResponse(questionId:1, roomId:1, rate:6) {
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
  createResponse(questionId:1, roomId:9, rate:2) {
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
