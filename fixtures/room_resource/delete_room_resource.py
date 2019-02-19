
null = None
delete_resource = '''
mutation {
    deleteResource(resourceId: 1) {
        resource {
            roomId
            id
            name
        }
    }
}
'''

expected_query_after_delete = {
    "data": {
        "deleteResource": {
            "resource": {
                "roomId": 1,
                "id": "1",
                "name": "Markers"
            }
        }
    }
}

delete_non_existant_resource = '''
mutation {
    deleteResource(resourceId: 12) {
        resource {
            roomId
            id
            name
        }
    }
}
'''

response_for_delete_room_resource_with_database_error = {
    "errors": [
        {
            "message": "There seems to be a database connection error, \
                contact your administrator for assistance",
            "locations": [
                {

                    "line": 3,
                    "column": 5
                }
                ],
            "path": [
                "deleteResource"
            ]
        }
    ],
    "data": {"deleteResource": null}}
