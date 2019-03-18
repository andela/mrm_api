true = True
false = False
null = None


all_questions_query = '''
query {
  questions{
    questions{
      id
      questionType
      questionTitle
      question
      startDate
      endDate
      questionResponseCount
      response {
        id
        questionId
        roomId
      }
    }
  }
}
'''

all_questions_query_response = {
    'data': {
        'questions': {
            'questions': [{
                'id': '1',
                'questionType': 'rate',
                'questionTitle': 'Rating Feedback',
                'question': 'How will you rate the brightness of the room',
                'startDate': '20 Nov 2018',
                'endDate': '28 Nov 2018',
                'questionResponseCount': 1,
                'response': [{
                    'id': '1',
                    'questionId': 1,
                    'roomId': 1
                }]
            },
                {
                'id': '2',
                'questionType': 'check',
                'questionTitle': 'check Feedback',
                'question':  'Is there anything missing in the room',
                'startDate': '20 Nov 2018',
                'endDate': '30 Nov 2018',
                'questionResponseCount': 1,
                'response': [{
                    'id': '2',
                    'questionId': 2,
                    'roomId': 1
                }]
            },
                {
                'id': '3',
                'questionType': 'input',
                'questionTitle': 'input Feedback',
                'question': 'Any other suggestion',
                'startDate': '20 Nov 2018',
                'endDate': '28 Nov 2018',
                'questionResponseCount': 0,
                'response': []
            }]
        }
    }
}

paginated_all_questions_query = '''
query {
  questions(page:1, perPage:2){
    questions{
      id
      questionType
      question
      startDate
      endDate
      questionResponseCount
      response {
        id
        questionId
        roomId
      }
    }
  }
}
'''

paginated_questions_empty_page = '''
query {
  questions(page:9, perPage:2){
    questions{
      id
      questionType
      question
      startDate
      endDate
      questionResponseCount
      response {
        id
        questionId
        roomId
      }
    }
  }
}
'''

paginated_all_questions_query_response = {
    'data': {
        'questions': {
            'questions': [{
                'id':
                '1',
                'questionType':
                'rate',
                'question':
                'How will you rate the brightness of the room',
                'startDate':
                '20 Nov 2018',
                'endDate':
                '28 Nov 2018',
                'questionResponseCount':
                1,
                'response': [{
                    'id': '1',
                    'questionId': 1,
                    'roomId': 1
                }]
            },
                {
                'id': '2',
                'questionType': 'check',
                'question':
                'Is there anything missing in the room',
                'startDate': '20 Nov 2018',
                'endDate': '30 Nov 2018',
                'questionResponseCount': 1,
                'response': [{
                    'id': '2',
                    'questionId': 2,
                    'roomId': 1
                }]
            }]
        }
    }
}

get_question_by_id_query = '''
query {
  question(id:1){
    id
    questionType
    question
    startDate
    endDate
    questionResponseCount
    response {
      id
      questionId
      roomId
    }
  }
}
'''

get_question_by_id_query_response = {
    'data': {
        'question': {
            'id': '1',
            'questionType': 'rate',
            'question': 'How will you rate the brightness of the room',
            'startDate': '20 Nov 2018',
            'endDate': '28 Nov 2018',
            'questionResponseCount': 1,
            'response': [{
                'id': '1',
                'questionId': 1,
                'roomId': 1
            }]
        }
    }
}

get_question_invalid_id_query = '''
query {
  question(id:122){
    id
    questionType
    question
    startDate
    endDate
    questionResponseCount
    response {
      id
      questionId
      roomId
    }
  }
}
'''

get_all_questions_query = '''
query {
  allQuestions(startDate: "2018 Nov 20", endDate: "2018 Nov 28"){
      questionType
  }
}
'''

get_all_questions_query_response = {
    "data": {
        "allQuestions": [
            {
                "questionType": "rate"
            }
        ]
    }
}

all_questions_higher_start_date_query = '''
query {
  allQuestions(startDate: "2018 Nov 28", endDate: "2018 Nov 20"){
      questionType
  }
}
'''

all_questions_query_no_date_range = '''
query {
  allQuestions {
      questionType
  }
}
'''

all_questions_query_no_date_range_response = {
    "data": {
        "allQuestions": [
            {
                "questionType": "rate"
            },
            {
                "questionType": "check"
            }
        ]
    }
}
