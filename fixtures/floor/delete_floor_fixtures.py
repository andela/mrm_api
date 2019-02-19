null = None
delete_floor_mutation = '''
    mutation {
        deleteFloor(floorId:4) {
            floor {
            name,
            blockId
            }
        }
    }
'''

delete_with_nonexistent_floor_id = '''
    mutation {
        deleteFloor(floorId:6) {
            floor {
            name,
            blockId
            }
        }
    }
'''

response_for_delete_floor_with_database_error = {
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
                "deleteFloor"
            ]
        }
    ],
    "data": {"deleteFloor": null}}
