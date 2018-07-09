
create_location_query = '''
    mutation {
  createLocation(name: "Kampala", abbreviation: "KLA", country: "Uganda", timeZone: "EAST_AFRICA_TIME") {   # noqa E501
    location {
      name
    }
  }
}
'''

create_location_response = {
    "data": {
        "createLocation": {
            "location": {
                "name": "Kampala"
            }
        }
    }
}
