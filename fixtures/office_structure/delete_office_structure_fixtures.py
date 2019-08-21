delete_node_by_id_mutation = """
mutation{
  deleteNode(nodeId:"C56A4180-65AA-42EC-A945-5FD21DEC0519"){
    node{
      id
      name
    }
  }
}
"""

delete_node_by_id_response = {
    "data": {
        "deleteNode": {
            "node": {
                "id": "c56a4180-65aa-42ec-a945-5fd21dec0519",
                "name": "Gold Coast",
            }
        }
    }
}


delete_node_invalid_id_mutation = """
mutation{
  deleteNode(nodeId:"C56A4180-65AA-42EC-A945-5FD21DEC0535"){
    node{
      id
      name
    }
  }
}
"""
