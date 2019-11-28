from .room_summary_response_fixture import response_sample

query_paginated_responses_empty_page = '''
    query{
  allRoomResponses(page:5, perPage:2){
   responses {
        roomName,
        totalResponses,
        response {
          id,
          response{
            ... on Rate{
              rate
            }
            ... on TextArea{
              suggestion
            }
            ... on SelectedOptions{
              options
            }
            ... on MissingItems{
              missingItems{
                name
              }
            }
          }
        }
      }
   hasNext
   hasPrevious
   pages
}
}
'''
query_paginated_responses_response = {
    "data": {
        "allRoomResponses": {
            "responses": response_sample,
            "hasNext": False,
            "hasPrevious": False,
            "pages": 1
        }
    }
}

query_paginated_responses = '''
    query{
  allRoomResponses(page:1, perPage:2){
   responses {
        roomName,
        totalResponses,
        response {
          id,
          response {
            ... on Rate{
              rate
            }
            ... on SelectedOptions{
              options
            }
            ... on TextArea{
              suggestion
            }
            ... on MissingItems{
              missingItems{
                name
              }
            }
          }
        }
      }
   hasNext
   hasPrevious
   pages
}
}
'''
