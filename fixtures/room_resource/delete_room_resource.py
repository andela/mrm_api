
null = None
delete_resource = '''
mutation {
    deleteResource(resourceId: 1) {
        resource {
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
            id
            name
        }
    }
}
'''
