resource_query = '''
    query {
        allResources{
                    resources{
                      name
                    }
              }
        }
'''

resource_query_response = {
  "data": {
    "allResources": {
      "resources": [
        {
          "name": "Markers"
        }
      ]
      }
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

get_paginated_room_resources = '''
 {
  allResources(page:1, perPage:2){
   resources{
      name
   }
   hasNext
   hasPrevious
   pages
}
}
'''

get_paginated_room_resources_response = {
  "data": {
    "allResources": {
      "resources": [
        {
          "name": "Chair"
        },
        {
          "name": "Speaker"
        }
      ],
      "hasNext": 'true',
      "hasPrevious": 'false',
      "pages": '2'
    }
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

get_room_resources_by_room_id_error_response = "Room has no resource yet"

filter_unique_resources = '''
query {
  allResources(unique: true){
   resources{
        name
        }
    }
}
    '''
filter_unique_resources_response = {
    "data": {
        "allResources": {
            "resources": [
                {
                    "name": "Markers"
                }
            ]
        }
    }
}
