
null = None
delete_resource ='''
mutation {
  deleteResource(name: "chair", roomId: 1, resourceId: 1) {
    resource {
      name
      roomId
      id
     
    }
  }
}
'''

expected_query_after_delete ={
  "data": {
    "deleteResource": {
      "resource": {
        "roomId": 1,
        "id": "UmVzb3VyY2U6MQ==",
        "name": "chair",
      }
    }
  }
}


