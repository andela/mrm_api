null = None

node_path_by_name_query = """
query {
  nodePathByName(nodeName: "Gold Coast", order: ASC) {
    name
    tag
  }
}
"""

node_path_by_name_response = {
    "data": {
        "nodePathByName": [
          {
            "name": "Epic Tower",
            "tag": "Lagos Building"
          },
          {
            "name": "Gold Coast",
            "tag": "First Floor"
          }
        ]
      }
    }


node_path_by_name_invalid_node_query = """
    query {
      nodePathByName(nodeName: "Kente", order: ASC) {
        name
        tag
      }
    }
    """
