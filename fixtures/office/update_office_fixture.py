null = None
update_office_with_wrong_ID_query = '''
    mutation {
        updateOffice(name: "The Crest", officeId:10 ) {
            office {
                name
                locationId
            }
        }
    }
'''

update_office_with_same_Name_query = '''
    mutation {
        updateOffice(name: "dojo", officeId:1 ) {
            office {
                name
                locationId
            }
        }
    }
'''
update_office_in_another_location_query = '''
    mutation {
        updateOffice(name: "The Crest", officeId:2 ) {
            office {
                name
                locationId
            }
        }
    }
'''

update_office_query = '''
    mutation {
        updateOffice(name: "Crest", officeId:1 ) {
            office {
                name
                locationId
            }
        }
    }
'''

office_mutation_response = {
    "data": {
        "updateOffice": {
            "office": {
                "name": "Crest",
                "locationId": 1,
            }
        }
    }
}
