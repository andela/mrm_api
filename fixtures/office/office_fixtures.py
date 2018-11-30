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


paginated_offices_query = '''
query {
    allOffices(page:1, perPage:3){
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
                },
                {
                    "name": "Epic tower",
                    "id": "3"
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
                },
                {
                    "name": "Epic tower",
                    "id": "3"
                }
            ]
        }
    }
}

paginated_offices_non_existing_page_query = '''
query {
    allOffices(page:5, perPage:3){
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
