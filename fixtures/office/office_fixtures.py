null = None
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

get_office_by_name = '''
query{
    getOfficeByName(name:"St. Catherines"){
        name
        id
        blocks{
            name
            floors{
                name
                id
                rooms{
                name
                  id
                    }
                    }
                    }
                }
        }
'''

get_office_by_name_response = {
    'data': {
        'getOfficeByName': [{
            'name': 'St. Catherines',
            'id': '1',
            'blocks': [{
                'name': 'EC',
                'floors': [{
                    'name': '3rd',
                    'id': '1',
                    'rooms': [{
                       'name': 'Entebbe',
                       'id': '1'}]
                }]
            }]
        }]
    }
    }
office_mutation_query_Different_Location = '''
    mutation {
        createOffice(name: "The Crest", locationId:2 ) {
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

office_mutation_query_non_existant_ID = '''
    mutation {
        createOffice(name: "The Crest", locationId:10 ) {
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
