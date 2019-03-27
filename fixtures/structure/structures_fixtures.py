null = None

query_structures = '''
    allStructures {
      web_id
      level
      name
      location
      position
      parent_id
      tag
    }
        '''

expected_response_structures = {
    "data": {
        "allStructures": [
            {
                "web_id": "azxtuvwertyuo",
                "level": "3",
                "name": "Epic Tower",
                "location": "1",
                "position": "1",
                "parent_id": "3",
                "tag": "Ilupeju"
            }
        ]
    }
}
