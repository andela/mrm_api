
create_location_query = '''
    mutation {
    createLocation(country: "Kenya",timeZone: "GMT+3",name: "Nairobi",  abbreviation: "NBO") { # noqa: E501
        location {
        abbreviation
        country
        name
        }
    }
    }
'''

create_location_response = {
    "data": {
        "createLocation": {
            "location": {
                "abbreviation": "NBO",
                "country": "Kenya",
                "name": "Nairobi"
            }
        }
    }
}
