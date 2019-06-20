null = None

create_suggestion_question = '''
mutation{
  createResponse(
    responses: [{questionId:3, textArea:"Any other suggestion"}], roomId:1) {
    response{
      id
      questionId
      roomId
      response
      }
  }
}
'''

create_suggestion_question_response = {
    "data": {
        "createResponse": {
            "response": [
                {
                    "id": "3",
                    "questionId": 3,
                    "roomId": 1,
                    "response": "Any other suggestion"
                }
            ]
        }
    }
}

make_suggestion_in_non_existent_room = '''
mutation{
  createResponse(
    responses: [{questionId:3, textArea:"Any other suggestion"}], roomId:90) {
    response{
      id
      questionId
      roomId
      response
      }
  }
}
'''

choose_wrong_question = '''
mutation{
  createResponse(
    responses: [{questionId:1, textArea:"Any other suggestion"}], roomId:1) {
    response{
      id
      questionId
      roomId
      response
      }
  }
}
'''
