
office_mutation_query = '''
    mutation {
        createOffice(buildingName: "EPIC Tower", locationId: 1){
            office {
                buildingName
                locationId
            }
        }
    }
'''

office_mutation_response = {
    "data": {
        "createOffice": {
            "office": {
                "buildingName": "EPIC Tower",
                "locationId": 1
            }
        }
    }
}
