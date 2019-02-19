create_location_query = '''
    mutation {
  createLocation(name: "New", abbreviation: "KLA", country: "Uganda", timeZone: "EAST_AFRICA_TIME", imageUrl:"https://lala.com") {   # noqa E501
    location {
      name
    }
  }
}
'''

create_location_query_wrong_country = '''
    mutation {
  createLocation(name: "New", abbreviation: "KLA", country: "Tanzania", timeZone: "EAST_AFRICA_TIME", imageUrl:"https://lala.com") {   # noqa E501
    location {
      name
    }
  }
}
'''

create_location_query_wrong_time_zone = '''
    mutation {
  createLocation(name: "New", abbreviation: "KLA", country: "Uganda", timeZone: "EAST_TIME", imageUrl:"https://lala.com") {   # noqa E501
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
null = None

response_for_create_location_with_database_error = {
    "errors": [
        {
            "message": "There seems to be a database connection error, \
                contact your administrator for assistance",
            "locations": [
                {

                    "line": 3,
                    "column": 3
                }
                ],
            "path": [
                "createLocation"
            ]
        }
    ],
    "data": {"createLocation": null}}
