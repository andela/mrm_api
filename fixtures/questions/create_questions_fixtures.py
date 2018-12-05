create_question_query = '''
 mutation{
  createQuestion(questionType:"Rating",
  question:"How will you rate the brightness of the room",
  startDate:"20 Nov 2018", endDate:"28 Nov 2018") {
    question{
      id
      question
      questionType
      startDate
      endDate
      }
  }
}
'''

create_question_response = {
  "data": {
    "createQuestion": {
      "question": {
        "id": "4",
        "question": "How will you rate the brightness of the room",
        "questionType": "Rating",
        "startDate": "20 Nov 2018",
        "endDate": "28 Nov 2018"
      }
    }
  }
}

question_mutation_query_without_name = '''
     mutation{
  createQuestion(questionType:"",
  question:"How will you rate the brightness of the room",
  startDate:"20 Nov 2018", endDate:"28 Nov 2018") {
    question{
      id
      question
      questionType
      startDate
      endDate
      }
  }
}
'''
