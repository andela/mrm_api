delete_assigned_resource_mutation = '''
    mutation {
        deleteAssignedResource(resourceId: 1, roomId: 1) {
            roomResource {
                roomId
                resourceId
            }
        }
    }
'''

delete_assigned_resource_from_non_existing_resource = '''
    mutation {
        deleteAssignedResource(resourceId: 10, roomId: 1) {
            roomResource {
                roomId
                resourceId
            }
        }
    }
'''

delete_assigned_resource_from_non_existing_room = '''
    mutation {
        deleteAssignedResource(resourceId: 1, roomId: 10) {
            roomResource {
                roomId
                resourceId
            }
        }
    }
'''

delete_non_existing_assigned_resource_mutation = '''
    mutation {
        deleteAssignedResource(resourceId: 1, roomId: 1) {
            roomResource {
                roomId
                resourceId
            }
        }
    }
'''

delete_assigned_resource_response = {
    "data": {
        "deleteAssignedResource": {
            "roomResource": {
                "roomId": "1",
                "resourceId": "1"
            }
        }
    }
}
