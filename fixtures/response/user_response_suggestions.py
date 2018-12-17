null = None

create_suggestion_question = '''
mutation{
  createResponse(questionId:3, roomId:1, textArea:"Any other suggestion") {
    response{
      id
      questionId
      roomId
      textArea
      }
  }
}
'''

create_suggestion_question_response = {
  "data": {
    "createResponse": {
      "response": {
        "id": "2",
        "questionId": 3,
        "roomId": 1,
        "textArea": "Any other suggestion"
      }
    }
  }
}

make_suggestion_in_non_existent_room = '''
mutation{
  createResponse(questionId:3, roomId:90, textArea:"Any other suggestion") {
    response{
      id
      questionId
      roomId
      textArea
      }
  }
}
'''

choose_wrong_question = '''
mutation{
  createResponse(questionId:1, roomId:1, textArea:"Any other suggestion") {
    response{
      id
      questionId
      roomId
      textArea
      }
  }
}
'''

choose_non_existent_question = '''
mutation{
  createResponse(questionId:8, roomId:1, textArea:"Any other suggestion") {
    response{
      id
      questionId
      roomId
      textArea
      }
  }
}
'''

make_suggestion_on_wrong_question = '''
mutation{
  createResponse(questionId:2, roomId:1, textArea:"Any other suggestion") {
    response{
      id
      questionId
      roomId
      textArea
      }
  }
}
'''
