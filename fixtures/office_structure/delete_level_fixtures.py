delete_level_fixtures = '''
mutation{
    deleteLevel(id:2){
        node{
        id
        }
    }
    }
'''

delete_level_response = {
  "data": {
    "deleteLevel": {
      "node": {
        "id": "2"
      }
    }
  }
}

delete_level_fixtures_non_existant_id = '''
mutation{
    deleteLevel(id:40){
        node{
        id
        }
    }
    }
'''

delete_level_fixtures_non_existant_id_response = '''
{
  "errors": [
    {
      "message": "Level not found",
      "locations": [
        {
          "line": 2,
          "column": 5
        }
      ],
      "path": [
        "deleteLevel"
      ]
    }
  ],
  "data": {
    "deleteLevel": null
  }
}
'''
