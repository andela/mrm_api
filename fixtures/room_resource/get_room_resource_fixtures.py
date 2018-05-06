resource_query = '''
    query {
        resources{
                    name
              }
        }
'''

resource_query_response = {
  "data": {
    "resources": [{
        "name": "Markers"
      }]
    }
  }