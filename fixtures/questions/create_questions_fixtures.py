import datetime

start_date = (
  datetime.datetime.now().replace(microsecond=0) + datetime.timedelta(days=1)
).isoformat()
end_date = (
  datetime.datetime.now().replace(microsecond=0) + datetime.timedelta(days=2)
).isoformat()
wrong_start_date = (
  datetime.datetime.now().replace(microsecond=0) + datetime.timedelta(days=-1)
).isoformat()
wrong_end_date = (
  datetime.datetime.now().replace(microsecond=0) + datetime.timedelta(days=1)
).isoformat()


create_question_query = '''
 mutation{{
  createQuestion(questionType:"Rate",
  question:"How will you rate the brightness of the room",
  startDate:"{}", endDate:"{}") {{
    question{{
      id
      question
      questionType
      startDate
      endDate
      }}
  }}
}}
'''.format(start_date, end_date)

create_question_query_with_early_startDate = create_question_query.replace(
  start_date, wrong_start_date
)

create_question_query_with_early_endDate = create_question_query.replace(
  end_date, wrong_end_date
)

create_question_response = {
  "data": {
    "createQuestion": {
      "question": {
        "id": "4",
        "question": "How will you rate the brightness of the room",
        "questionType": "rate",
        "startDate": start_date.replace('T', ' '),
        "endDate": end_date.replace('T', ' ')
      }
    }
  }
}

question_mutation_query_without_name = '''
     mutation{{
  createQuestion(questionType:"",
  question:"How will you rate the brightness of the room",
  startDate:"{}", endDate:"{}") {{
    question{{
      id
      question
      questionType
      startDate
      endDate
      }}
  }}
}}
'''.format(start_date, end_date)

update_question_mutation = '''
  mutation {{
      updateQuestion(questionId:1,
      startDate:"{}", endDate:"{}") {{
        question {{
          id,
          startDate,
          endDate,
        }}
      }}
  }}
'''.format(start_date, end_date)

update_question_response = {
  "data": {
    "updateQuestion": {
      "question": {
        "id": "1",
        "startDate": start_date.replace('T', ' '),
        "endDate": end_date.replace('T', ' '),
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
