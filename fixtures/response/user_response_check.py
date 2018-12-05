null = None

check_non_existing_question = '''
mutation{
  createResponse(questionId:5, roomId:1, check:true) {
    response{
      id
      questionId
      roomId
      check
      }
  }
}
'''

check_non_existing_question_response = {
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

check_with_non_existent_room = '''
mutation{
  createResponse(questionId:2, roomId:9, check:true) {
    response{
      id
      questionId
      roomId
      check
      }
  }
}
'''

create_check_query = '''
mutation{
  createResponse(questionId:2, roomId:1, check:true) {
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
      "response": {
        "id": "10",
        "questionId": 2,
        "roomId": 1
      }
    }
  }
}

select_check_question = '''
mutation{
  createResponse(questionId:1, roomId:1, check:true) {
    response{
      id
      questionId
      roomId
      check
      }
  }
}
'''
