null = None
query_update_all_fields = '''mutation{
    updateLocation(locationId: 1, name: "Kampala", country: "Kenya", abbreviation: "KE"){ # noqa: E501
        location{
            name
            abbreviation
            country
        }
    }
}
'''

expected_query_update_all_fields = {
    "data": {
        "updateLocation": {
            "location": {
                "name": "Kampala",
                "abbreviation": "KE",
                "country": "CountryType.Kenya"
            }
        }
    }
}

query_location_id_non_existant = '''mutation{
  updateLocation(
    locationId: 7,
    timeZone: "EAST_AFRICA_TIME",
    name: "Kigali",
    country: "Kenya",
    abbreviation: "KE"){
    location{
      name
      id
      }
  }
}
'''
expected_location_id_non_existant_query = {
     "errors": [{
      "message": "Location not found",
      "locations": [
        {
          "line": 2,
          "column": 3
        }
      ],
      "path": ["updateLocation"]
       }],
      "data": {
      "updateLocation": null}
}

query_update_location_invalid_timezone = '''mutation {
    updateLocation(
    locationId: 1,
    timeZone: "ABC",
    name: "Kigali",
    country: "Kenya",
    abbreviation: "KE"){
    location{
      name
      id
      }
  }
}
'''

query_update_location_invalid_image_url = '''mutation {
    updateLocation(
    locationId: 1,
    imageUrl: "http;//",
    name: "Kigali",
    country: "Kenya",
    abbreviation: "KE"){
    location{
      name
      id
      }
  }
}
'''
