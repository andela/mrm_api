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
    'errors': [{
        'message': 'Office created but Emails not Sent',
        'locations': [{
            'line': 3,
            'column': 9
        }],
        'path': ['createOffice']
    }],
    'data': {
        'createOffice': None
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

office_mutation_query_duplicate_name = '''
    mutation {
        createOffice (name: "St. Catherines", locationId: 1) {
            office {
                name
            }
        }
    }
'''

office_mutation_query_duplicate_name_responce = {
    "errors": [
        {
            "message": "St. Catherines Office already exists",
            "locations": [
                {
                    "line": 3,
                    "column": 9
                }
            ],
            "path": [
                "createOffice"
            ]
        }
    ],
    "data": {
        "createOffice": null
    }
}

delete_office_mutation = '''
mutation{
    deleteOffice(officeId: 1){
        office{
            name
            blocks{
                name
                floors{
                    name
                    rooms{
                        name
                        roomType
                        capacity
                        resources{
                            name
                            quantity
                            devices{
                                name
                            }
                        }
                    }
                }
            }
        }
    }
}
'''

delete_office_mutation_response = {
    "data": {
        "deleteOffice": {
            "office": {
                "name": "St. Catherines",
                "blocks": [
                    {
                        "name": "EC",
                        "floors": [
                            {
                                "name": "3rd",
                                "rooms": [
                                    {
                                        "name": "Entebbe",
                                        "roomType": "meeting",
                                        "capacity": 6,
                                        "resources": [
                                            {
                                                "name": "Markers",
                                                "quantity": 3,
                                                "devices": [
                                                    {
                                                        "name": "Samsung"
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        }
    }
}

delete_non_existent_office_mutation = '''

mutation{
    deleteOffice(officeId: 10){
        office{
            name
        }
    }
}

'''

delete_unauthorised_location_mutation = '''
mutation{
    deleteOffice(officeId: 2){
        office{
            name
        }
    }
}
'''

paginated_offices_query = '''
query {
    allOffices(page:1, perPage:2){
        offices{
            name
            id
        }
        hasNext
        hasPrevious
        pages
    }
}
'''
offices_query_response = {
    "data": {
        "allOffices": {
            "offices": [
                {
                    "name": "St. Catherines",
                    "id": "1"
                },
                {
                    "name": "dojo",
                    "id": "2"
                }
            ],
            "hasNext": False,
            "hasPrevious": False,
            "pages": 1
        }
    }
}

offices_query = '''
query {
    allOffices{
        offices{
            name
            id
        }
    }
}
'''
all_offices_query_response = {
    "data": {
        "allOffices": {
            "offices": [
                {
                    "name": "St. Catherines",
                    "id": "1"
                },
                {
                    "name": "dojo",
                    "id": "2"
                }
            ]
        }
    }
}

paginated_offices_non_existing_page_query = '''
query {
    allOffices(page:2, perPage:2){
        offices{
            name
            id
        }
        hasNext
        hasPrevious
        pages
    }
}
'''
