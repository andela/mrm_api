create_location_query = '''
    mutation {
  createLocation(name: "New", abbreviation: "KLA", country: "Uganda", timeZone: "EAST_AFRICA_TIME", imageUrl:"https://lala.com") {   # noqa E501
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
                "name": "New"
            }
        }
    }
}

create_duplicate_location_response = '''
{
  "errors": [
    {
      "message": "New Location already exists",
      "locations": [
        {
          "line": 2,
          "column": 3
        }
      ],
      "path": [
        "createLocation"
      ]
    }
  ],
  "data": {
    "createLocation": null
  }
}
'''
