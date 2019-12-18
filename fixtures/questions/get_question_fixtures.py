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
