null = None

update_floor_mutation = '''
    mutation {
        updateFloor(floorId:4, name:"2nd") {
            floor {
            name,
            blockId
            }
        }
    }
    '''

update_floor_mutation_response = {
  "data": {
    "updateFloor": {
      "floor": {
        "name": "2nd",
        "blockId": 1
      }
    }
  }
}

update_with_empty_field = '''
    mutation {
        updateFloor(floorId:4, name:"") {
            floor {
            name,
            blockId
            }
        }
    }
    '''

floor_mutation_duplicate_name = '''
    mutation {
        updateFloor(name: "3rd", floorId:4) {
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
        "updateFloor"
      ]
    }
  ],
  "data": {
    "updateFloor": null
  }
}

update_with_nonexistent_floor_id = '''
    mutation {
        updateFloor(floorId:8, name:"2nd") {
            floor {
            name,
            blockId
            }
        }
    }
    '''

response_for_update_floor_with_database_error = {
    "errors": [
        {
            "message": "There seems to be a database connection error, \
                contact your administrator for assistance",
            "locations": [
                {

                    "line": 3,
                    "column": 9
                }
                ],
            "path": [
                "updateFloor"
            ]
        }
    ],
    "data": {"updateFloor": null}}
