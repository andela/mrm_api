create_question_query = '''
 mutation{
  createQuestion(questionType:"Rate",
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
        "questionType": "rate",
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

update_question_mutation = '''
  mutation {
      updateQuestion(questionId:1,
      startDate:"12th Dec, 2018", endDate:"18th Dec, 2018") {
        question {
          id,
          startDate,
          endDate,
        }
      }
  }
'''

update_question_response = {
  "data": {
    "updateQuestion": {
      "question": {
        "id": "1",
        "startDate": "12th Dec, 2018",
        "endDate": "18th Dec, 2018",
      }
    }
  }
}

update_question_invalidId = '''
 mutation{
  updateQuestion(questionId:100,
  question:"How will you rate the brightness of the room") {
    question{
      id
      question
    }
  }
}
'''

delete_question_mutation = '''
 mutation{
  deleteQuestion(questionId:1) {
    question{
      id
    }
  }
}
'''

delete_question_response = {
  "data": {
    "deleteQuestion": {
      "question": {
        "id": "1"
      }
    }
  }
}

delete_question_invalidId = '''
 mutation{
  deleteQuestion(questionId:100) {
    question{
      id
    }
  }
}
'''
