null = None

query_structures = '''
   {
      allStructures {
        webId
        level
        name
        parentId
        tag
        locationId
        position
      }
    }
        '''

expected_response_structures = {
    "data": {
        "allStructures": [
            {
                "webId": "b05fc5f2-b4aa-4f48-a8fb-30bdcc3fc968",
                "level": 1,
                "name": "Epic tower",
                "parentId": 1,
                "tag": "Building",
                "locationId": 1,
                "position": 1
            }
        ]
    }
}
