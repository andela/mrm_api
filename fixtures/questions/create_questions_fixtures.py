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
  questionTitle:"Rating Feedback",
  question:"How will you rate the cleanliness of the room",
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
        "question": "How will you rate the cleanliness of the room",
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
  questionTitle:"Rating"
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

question_mutation_query_with_invalid_question_type = '''
 mutation{{
  createQuestion(questionType:"Rates",
  questionTitle:"Rating Feedback",
  question:"How will you rate the cleanliness of the room",
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
      questionTitle:"Rating Feedback"
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
  questionTitle:"Rating Feedback"
  question:"How will you rate the brightness of the room") {
    question{
      id
      question
    }
  }
}
'''

update_question_with_invalid_question_type = '''
  mutation {{
      updateQuestion(questionId:1,
      questionType: "Rates"
      questionTitle:"Rating Feedback"
      startDate:"{}", endDate:"{}") {{
        question {{
          id,
          startDate,
          endDate,
        }}
      }}
  }}
'''.format(start_date, end_date)

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
all_questions_query = '''
query {
    allQuestions{
        question
        id
        questionType
    }
}
'''
all_questions_response = {
    "data": {
        "allQuestions": [
            {
                "question": "How will you rate the brightness of the room",
                "id": "1",
                "questionType": "rate"
            },
            {
                'question': 'Is there anything missing in the room',
                'id': '2',
                'questionType': 'check'
            },
            {
                'question': 'Any other suggestion',
                'id': '3',
                'questionType': 'input'
            }
        ]
    }
}

query_update_total_views_of_questions = '''
mutation{
  updateQuestionViews(incrementTotalViews:true) {
    questions{
      question
      questionType
      totalViews
      }
  }
}
'''
