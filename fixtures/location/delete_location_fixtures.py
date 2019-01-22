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
