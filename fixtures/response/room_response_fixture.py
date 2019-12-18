import datetime

null = None

start_date = (datetime.date.today() - datetime.timedelta(
    days=2)).strftime('%b %d %Y')
end_date = datetime.date.today().strftime('%b %d %Y')
invalid_start_date = (datetime.date.today() + datetime.timedelta(
    days=10)).strftime('%b %d %Y')
invalid_end_date = (datetime.date.today() + datetime.timedelta(
    days=20)).strftime('%b %d %Y')

room_response_query_sample = '''{
    roomResponse(roomId:1) {
        roomName,
        totalResponses,
        response{
            responseId,
            createdDate,
            suggestion,
            rating
        }
    }
}
'''

get_room_response_query = '''{
    roomResponse(roomId:1) {
        roomName,
        totalResponses
    }
}
'''

get_room_response_query_data = {
    "data": {
        "roomResponse": {
            "roomName": "Entebbe",
            "totalResponses": 2
        }
    }
}

get_resolved_room_responses_query = '''{
    roomResponse(roomId:1, resolved:true) {
        roomName,
        totalResponses
    }
}
'''

get_resolved_room_responses_query_data = {
    "data": {
        "roomResponse": {
            "roomName": "Entebbe",
            "totalResponses": 1
        }
    }
}

get_room_response_query_by_date = '''
query{{
    allRoomResponses(startDate: "{}",
     endDate: "{}" ){{
        responses{{
            totalResponses
            roomName
            response{{
                id
                response{{
                  ... on Rate{{
                    rate
                  }}
                  ... on SelectedOptions{{
                    options
                  }}
                  ... on TextArea{{
                    suggestion
                  }}
                  ... on MissingItems{{
                    missingItems{{
                      name
                    }}
                  }}
                  }}
            }}
        }}
    }}
}}
'''.format(start_date, end_date)

get_room_response_query_by_date_and_limits = '''
query{{
    allRoomResponses(startDate: "{}",
     endDate: "{}",
     upperLimitCount: 3, lowerLimitCount: 0,
     room:"Entebbe" ){{
        responses{{
            totalResponses
            roomName
            response{{
                id
                response{{
                  ... on Rate{{
                    rate
                  }}
                  ... on SelectedOptions{{
                    options
                  }}
                  ... on TextArea{{
                    suggestion
                  }}
                  ... on MissingItems{{
                    missingItems{{
                      name
                    }}
                  }}
                  }}
            }}
        }}
    }}
}}
'''.format(start_date, end_date)

get_room_response_query_with_invalid_date = '''
query{{
    allRoomResponses(startDate: "{}",
     endDate: "{}" ){{
        responses{{
            totalResponses
            roomName
            response{{
                id
                response{{
                  ... on Rate{{
                    rate
                  }}
                  ... on SelectedOptions{{
                    options
                  }}
                  ... on TextArea{{
                    suggestion
                  }}
                  ... on MissingItems{{
                    missingItems{{
                      name
                    }}
                  }}
                  }}
            }}
        }}
    }}
}}
'''.format(invalid_start_date, invalid_end_date)

get_room_response_query_with_higher_start_date = '''
query{{
    allRoomResponses(startDate: "{}",
     endDate: "{}" ){{
        responses{{
            totalResponses
            roomName
            response{{
                id
                response{{
                  ... on Rate{{
                    rate
                  }}
                  ... on SelectedOptions{{
                    options
                  }}
                  ... on TextArea{{
                    suggestion
                  }}
                  ... on MissingItems{{
                    missingItems{{
                      name
                    }}
                  }}
                  }}
            }}
        }}
    }}
}}
'''.format(end_date, start_date)

get_room_response_query_by_date_data = {
    "data": {
        "allRoomResponses": {
            "responses": [
                {
                    "totalResponses": 2,
                    "roomName": "Entebbe",
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
        }
    }
}


get_room_response_non_existence_room_id = '''{
    roomResponse(roomId:15) {
        roomName,
        totalResponses,
        response{
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
}
'''
