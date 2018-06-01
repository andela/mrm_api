resource_query = '''
    query {
        allResources{
                    name
              }
        }
'''

resource_query_response = {
  "data": {
    "allResources": [{
        "name": "Markers"
      }]
    }
  }

get_room_resources_by_room_id = '''
{
    getResourcesByRoomId(roomId: 1){
        roomId
        name
    }
}
'''

get_room_resources_by_room_id_response = {
  "data": {
    "getResourcesByRoomId": [
      {
        "roomId": 1,
        "name": "Markers"
      }
    ]
  }
}

get_room_resources_by_room_id_error = '''
{
    getResourcesByRoomId(roomId: 100){
        roomId
        name
    }
}
'''

get_room_resources_by_room_id_error_response = {
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
    "getResourcesByRoomId": None
  }
}
