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

create_duplicate_location_query = '''
mutation {
  createLocation(
    name: "Kampala", abbreviation: "KLA", country: "Uganda",
    timeZone: "EAST_AFRICA_TIME", imageUrl:"https://lala.com") {
    location {
      name
    }
  }
}
'''

create_location_with_invalid_url = '''
    mutation {
  createLocation (
    name: "New", abbreviation: "KLA", country: "Uganda",
    timeZone: "EAST_AFRICA_TIME", imageUrl:"https://") {
    location {
      name
    }
  }
}
'''

create_location_with_invalid_timezone = '''
    mutation {
  createLocation (
    name: "New", abbreviation: "KLA", country: "Uganda",
    timeZone: "AMERICAN_TIMEZONE", imageUrl:"https://lala.com") {
    location {
      name
    }
  }
}
'''
