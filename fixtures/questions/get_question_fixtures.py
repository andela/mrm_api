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
