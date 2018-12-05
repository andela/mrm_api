null = None

create_rate_query = '''
mutation{
  createRate(questionId:1, roomId:1, rate:2) {
    rating{
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
    "createRate": {
      "rating": {
        "id": "1",
        "questionId": 1,
        "roomId": 1,
        "rate": 2
      }
    }
  }
}

rate_wrong_question = '''
mutation{
  createRate(questionId:2, roomId:1, rate:2) {
    rating{
      id
      questionId
      roomId
      rate
      userId
      }
  }
}
'''

rate_wrong_question_response = {
  "errors": [
    {
      "message": "Select a rating question",
      "locations": [
        {
          "line": 2,
          "column": 3
        }
      ],
      "path": [
        "createRate"
      ]
    }
  ],
  "data": {
    "createRate": null
  }
}

rate_non_existing_question = '''
mutation{
  createRate(questionId:5, roomId:1, rate:2) {
    rating{
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
        "createRate"
      ]
    }
  ],
  "data": {
    "createRate": null
  }
}

invalid_rating_number = '''
mutation{
  createRate(questionId:1, roomId:1, rate:6) {
    rating{
      id
      questionId
      roomId
      rate
      userId
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
        "createRate"
      ]
    }
  ],
  "data": {
    "createRate": null
  }
}


rate_with_non_existent_room = '''
mutation{
  createRate(questionId:1, roomId:9, rate:2) {
    rating{
      id
      questionId
      roomId
      rate
      userId
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
        "createRate"
      ]
    }
  ],
  "data": {
    "createRate": null
  }
}
