null = None

create_suggestion_question = '''
mutation{
  createSuggestion(questionId:3, roomId:1, textArea:"Any other suggestion") {
    suggestion{
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
    "createSuggestion": {
      "suggestion": {
        "id": "1",
        "questionId": 3,
        "roomId": 1,
        "textArea": "Any other suggestion"
      }
    }
  }
}

make_suggestion_in_non_existent_room = '''
mutation{
  createSuggestion(questionId:3, roomId:90, textArea:"Any other suggestion") {
    suggestion{
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
  createSuggestion(questionId:1, roomId:1, textArea:"Any other suggestion") {
    suggestion{
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
  createSuggestion(questionId:8, roomId:1, textArea:"Any other suggestion") {
    suggestion{
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
  createSuggestion(questionId:2, roomId:1, textArea:"Any other suggestion") {
    suggestion{
      id
      questionId
      roomId
      textArea
      }
  }
}
'''
