resource_query = '''
    query {
        resources{
            edges{
                node{
                    name
                }
            }
        }
    }
'''

resource_query_response = {
  "data": {
    "resources": {
      "edges": [
        {
          "node": {
            "name": "Markers"
          }
        }
      ]
    }
  }
}