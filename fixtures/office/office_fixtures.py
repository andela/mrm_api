office_mutation_query = '''
    mutation {
        createOffice(name: "The Crest", locationId:1 ) {
            office {
                name
                locationId
                blocks {
                    id
                    name
                }
            }
        }
    }
'''

office_mutation_response = {
    "data": {
        "createOffice": {
            "office": {
                "name": "The Crest",
                "locationId": 1,
                "blocks": [
                    {
                        "id": '2',
                        "name": "The Crest"
                    }
                ]
            }
        }
    }
}
