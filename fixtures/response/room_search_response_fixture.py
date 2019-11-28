from ..output.OutputBuilder import build

room_response_data = {
    "allRoomResponses": {
        "responses": [
            {
                "roomName": "Entebbe",
                "totalResponses": 1,
                "response": [
                        {
                            "id": 2,
                            "response": {
                                "options": [
                                    "marker pen",
                                    "apple tv"
                                ]
                            }
                        }
                ]
            }
        ]
    }
}

search_resolved_responses_by_room_name_data = build(
    data=room_response_data
)


search_resolved_responses_by_room_name = '''
query{
    allRoomResponses(room:"Entebbe", resolved:true){
        responses{
            totalResponses
            roomName
            response{
                id
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

search_response_by_room_no_response = '''
query{
    allRoomResponses(room:"Kampala"){
        responses{
            totalResponses
            roomId
            roomName
            response{
                id
            }
        }
    }
}
'''

search_response_by_invalid_room = '''
query{
    allRoomResponses(room:"Mubende"){
        responses{
            totalResponses
            roomName
            response{
                id
            }
        }
    }
}
'''
search_response_by_room_invalid_room_query = '''
query{
    allRoomResponses(upperLimitCount: 2, lowerLimitCount: 0, room:"Entebbes"){
        responses{
            totalResponses
            roomName
            response{
                id
            }
        }
    }
}
'''

search_response_by_room_only = '''
query{
    allRoomResponses(room:"Entebbe"){
        responses{
            totalResponses
            roomName
            response{
                id
            }
        }
    }
}
'''

search_response_by_room_query = '''
 query{
    allRoomResponses(lowerLimitCount: 1, upperLimitCount: 3, room:"Entebbe"){
        responses{
            totalResponses
            roomName
            response{
                id
            }
        }
    }
}
'''

search_response_by_room_beyond_limits_query = '''
query{
    allRoomResponses(upperLimitCount: 7, lowerLimitCount: 5, room:"Entebbe"){
        responses{
            totalResponses
            roomName
            response{
                id
            }
        }
    }
}
'''
