true = True
false = False
null = None

get_question_query = '''{
  feedbackQuestion {
    totalResponses
    responses {
      roomName,
      responseCount,
      cleanlinessRating
    }
  }
}
'''

get_question_query_response = {
  "data": {
    "feedbackQuestion": {
      "totalResponses": 1,
      "responses": [
        {
          "roomName": "Entebbe",
          "responseCount": 1,
          "cleanlinessRating": 2
        }
      ]
    }
  }
}

get_paginated_question = '''{
  feedbackQuestion(page:1, perPage:1) {
    hasNext,
    hasPrevious,
    pages
    totalResponses
    responses {
      roomName,
      responseCount,
      cleanlinessRating
    }
  }
}
'''

get_paginated_question_query_response = {
  "data": {
    "feedbackQuestion": {
      "hasNext": false,
      "hasPrevious": false,
      "pages": 1,
      "totalResponses": 1,
      "responses": [
        {
          "roomName": "Entebbe",
          "responseCount": 1,
          "cleanlinessRating": 2
        }
      ]
    }
  }
}

get_paginated_question_invalid_page = '''{
  feedbackQuestion(page:100, perPage:5) {
    hasNext,
    hasPrevious,
    pages
    totalResponses
    responses {
      roomName,
      responseCount,
      cleanlinessRating
    }
  }
}
'''
