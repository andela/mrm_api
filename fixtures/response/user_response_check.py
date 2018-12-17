null = None

check_non_existing_question = '''
mutation{
  createCheck(questionId:5, roomId:1, check:true) {
    checking{
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
        "createCheck"
      ]
    }
  ],
  "data": {
    "createCheck": null
  }
}

check_with_non_existent_room = '''
mutation{
  createCheck(questionId:2, roomId:9, check:true) {
    checking{
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
  createCheck(questionId:2, roomId:1, check:true) {
    checking{
      id
      questionId
      roomId
      }
  }
}
'''

create_check_response = {
  "data": {
    "createCheck": {
      "checking": {
        "id": "10",
        "questionId": 2,
        "roomId": 1
      }
    }
  }
}

select_check_question = '''
mutation{
  createCheck(questionId:1, roomId:1, check:true) {
    checking{
      id
      questionId
      roomId
      check
      }
  }
}
'''
