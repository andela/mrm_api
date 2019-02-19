null = None

delete_location_query = '''
    mutation{
    deleteLocation(locationId:1){
        location{
        id
        }
    }
    }
'''

delete_location_response = {

  "data": {
    "deleteLocation": {
      "location": {
        "id": "1"
      }
    }
  }
}

delete_non_existent_location = '''
mutation{
  deleteLocation(locationId:10){
    location{
      id
    }
  }
}
'''

response_for_delete_location_with_database_error = {
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
                "deleteLocation"
            ]
        }
    ],
    "data": {"deleteLocation": null}}
