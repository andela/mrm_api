null = None

update_floor_mutation = '''
    mutation {
        updateFloor(floorId:1, name:"2nd") {
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
        updateFloor(floorId:1, name:"") {
            floor {
            name,
            blockId
            }
        }
    }
    '''

floor_mutation_duplicate_name = '''
    mutation {
        updateFloor(name: "3rd", floorId:1) {
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
