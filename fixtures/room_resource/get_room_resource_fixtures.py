resource_query = '''
    query {
        resources{
                    name
              }
        }
'''

resource_query_response = {
  "data": {
    "resources": [{
        "name": "Markers"
      }]
    }
  }

get_room_resource_by_room_id = '''
{
    getResourceByRoomId(roomId: 1){
        roomId
        name
    }
}
'''

get_room_resource_by_room_id_response = {
  "data": {
    "getResourceByRoomId": [
      {
        "roomId": 1,
        "name": "Markers"
      }
    ]
  }
}

get_room_resource_by_room_id_error = '''
{
    getResourceByRoomId(roomId: 100){
        roomId
        name
    }
}
'''

get_room_resource_by_room_id_error_response = {
  "errors": [
    {
      "message": "Room has no resource yet",
      "locations": [
        {
          "line": 3,
          "column": 5
        }
      ]
    }
  ],
  "data": {
    "getResourceByRoomId": None
  }
}
