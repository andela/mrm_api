null = None

create_floor_mutation = '''
    mutation {
        createFloor(name: "2nd", blockId:1) {
            floor {
            name
            blockId
            }
        }
    }
    '''

create_floor_mutation_response = {
        "data": {
            "createFloor": {
                "floor": {
                    "name": "2nd",
                    "blockId": 1
                }
            }
        }
    }

floor_name_empty_mutation = '''
    mutation {
        createFloor(name: "", blockId:1) {
            floor {
                name
                blockId
            }
        }
    }
'''

create_with_nonexistent_block_id = '''
    mutation {
        createFloor(name: "2nd", blockId:8) {
            floor {
            name
            blockId
            }
        }
    }
    '''

floor_mutation_duplicate_name = '''
    mutation {
        createFloor(name: "3rd", blockId:1) {
            floor {
            name
            blockId
            }
        }
    }
    '''

floor_mutation_duplicate_name_response = {
  "errors": [
    {
      "message": "3rd Floor already exists",
      "locations": [
        {
          "line": 3,
          "column": 9
        }
      ],
      "path": [
        "createFloor"
      ]
    }
  ],
  "data": {
    "createFloor": null
  }
}
