
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
