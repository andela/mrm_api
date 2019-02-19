null = None

check_non_existing_question = '''
mutation{
  createResponse(responses: [{questionId:5, missingItems:[1]}], roomId:1) {
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
      check
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

create_check_query_non_existence_item = '''
mutation{
  createResponse(responses: [{questionId:2, missingItems:[10]}], roomId:1) {
    response{
      id
      questionId
      roomId
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
        "getRoomResponse": [
          {
            "room": {
              "capacity": 6,
              "name": "Entebbe",
              "roomType": "meeting"
            }
          },
          {
            "room": {
              "capacity": 6,
              "name": "Entebbe",
              "roomType": "meeting"
            }
          }
        ]
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
