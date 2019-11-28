summary_room_response_query = '''{
    allRoomResponses {
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
                id
              }
            }
          }
        }
      }
    }
}
'''

response_sample = [
    {
        "roomName": "Entebbe",
                    "totalResponses": 2,
                    "response": [
                        {
                            "id": 2,
                            "response": {
                                "options": [
                                    "marker pen",
                                    "apple tv"
                                ]
                            }
                        },
                        {
                            "id": 1,
                            "response": {
                                "rate": 1
                            }
                        }
                    ]
    }
]

summary_room_response_data = {
    "data": {
        "allRoomResponses": {
            "responses": response_sample
        }
    }
}
