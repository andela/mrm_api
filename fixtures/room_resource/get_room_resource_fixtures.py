null = None

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
                    "name": "Markers"
                }
            ],
            "hasNext":  False,
            "hasPrevious": False,
            "pages": 1
        }
    }
}

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

get_paginated_resources = '''
query {
  allResources(page:1, perPage:1){
   resources {
    name
    id
  }
   hasNext
   hasPrevious
   pages
}
}
'''

get_paginated_resources_response = {
    "data": {
        "allResources": {
            "resources": [
                {
                    "name": "Notepads",
                    "id": "1"
                }
            ],
            "hasNext": False,
            "hasPrevious": False,
            "pages": 1
        }
    }
}

get_paginated_resources_past_page = '''
query {
  allResources(page:2, perPage:1){
   resources {
    name
    id
  }
   hasNext
   hasPrevious
   pages
}
}
'''
get_paginated_resources_inexistent_page = '''
query {
  allResources(page:-1, perPage:1){
   resources {
    name
    id
  }
   hasNext
   hasPrevious
   pages
}
}
'''
