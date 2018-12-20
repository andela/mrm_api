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

filter_question_by_room = '''
{
  getRoomResponse(roomId: 1) {
    room {
      capacity
      name
      roomType
    }
  }
}
'''

filter_question_by_room_response = {
    "data": {
        "getRoomResponse": [{
            "room": {
                "capacity": 6,
                "name": "Entebbe",
                "roomType": "meeting"
            }
        }]
    }
}

filter_question_by_invalid_room = '''
{
  getRoomResponse(roomId: 100) {
    room {
      id
      name
      roomType
    }
  }
}

'''

filter_question_by_invalid_room_response = {
    "errors": [{
        "message": "No Feedback Found",
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
