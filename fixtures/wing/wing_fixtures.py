null = None

create_wing_mutation = '''
    mutation {
        createWing(name: "Ginger bread" floorId:5) {
            wing {
                id
                name
            }
        }
    }
'''

create_wing_mutation_response = {
    "data": {
        "createWing": {
            "wing": {
                "id": "3",
                "name": "Ginger Bread"
            }
        }
    }
}

duplicate_wing_mutation = '''
    mutation {
        createWing(name: "Naija" floorId:5) {
            wing {
                id
                name
            }
        }
    }
'''

duplicate_wing_mutation_response = {
    "errors": [
        {
            "message": "Naija Wing already exists",
            "locations": [
                {
                    "line": 3,
                    "column": 9
                }
            ],
            "path": [
                "createWing"
            ]
        }
    ],
    "data": {
        "createWing": null
    }
}

wing_creation_no_name = '''
    mutation {
        createWing(name: "" floorId:4) {
            wing {
                id
                name
            }
        }
    }
'''

wing_creation_no_name_response = {
    "errors": [
        {
            "message": "name is required field",
            "locations": [
                {
                    "line": 3,
                    "column": 9
                }
            ],
            "path": [
                "createWing"
            ]
        }
    ],
    "data": {
        "createWing": null
    }
}

create_wing_other_location = '''
    mutation {
        createWing(name: "New" floorId:4) {
            wing {
                id
                name
            }
        }
    }
'''

create_wing_other_location_admin = '''
    mutation {
        createWing(name: "New" floorId:4) {
            wing {
                id
                name
            }
        }
    }
'''

create_wing_floor_not_found = '''
    mutation {
        createWing(name: "New" floorId:18) {
            wing {
                id
                name
            }
        }
    }
'''

update_wing_mutation = '''
    mutation {
        updateWing(name: "Oshodi" wingId:1) {
            wing {
                id
                name
            }
        }
    }
'''

update_wing_response = {
    "data": {
        "updateWing": {
            "wing": {
                "id": "1",
                "name": "Oshodi"
            }
        }
    }
}

update_duplicate_wing_mutation = '''
    mutation {
        updateWing(name: "Naija" wingId:2) {
            wing {
                id
                name
            }
        }
    }
'''

update_duplicate_wing_mutation_response = {
    "errors": [
        {
            "message": "Naija Wing already exists",
            "locations": [
                {
                    "line": 3,
                    "column": 9
                }
            ],
            "path": [
                "updateWing"
            ]
        }
    ],
    "data": {
        "updateWing": null
    }
}

wing_update_no_name = '''
    mutation {
        updateWing(name: "" wingId:1) {
            wing {
                id
                name
            }
        }
    }
'''

update_wing_id_not_found = '''
    mutation {
        updateWing(name: "New" wingId:100) {
            wing {
                id
                name
            }
        }
    }
'''

delete_wing_mutation = '''
    mutation{
    deleteWing(wingId: 1){
        wing{
            name
        }
    }
}
'''

delete_wing_response = {
    "data": {
        "deleteWing": {
            "wing": {
                "name": "Naija"
            }
        }
    }
}

delete_wing_id_not_found = '''
    mutation{
    deleteWing(wingId: 5){
        wing{
            name
        }
    }
}
'''

get_all_wings_query = '''query {
    allWings {
        wings {
            id
            name
            floorId
        }
    }
}
'''

get_all_wings_query_response = {
    "data": {
        "allWings": {
            "wings": [
                {
                    "id": "1",
                    "name": "Naija",
                    "floorId": 5
                },
                {
                    "id": "2",
                    "name": "Big Apple",
                    "floorId": 5
                }
            ]
        }
    }
}

paginated_wings_query = '''query {
    allWings(page: 1, perPage: 2) {
        wings {
            id
            name
            floorId
        }
        queryTotal
        pages
        hasNext
        hasPrevious
    }
}
'''

paginated_wings_query_response = {
    "data": {
        "allWings": {
            "wings": [
                {
                    "id": "1",
                    "name": "Naija",
                    "floorId": 5
                },
                {
                    "id": "2",
                    "name": "Big Apple",
                    "floorId": 5
                }
            ],
            "queryTotal": 2,
            "pages": 1,
            "hasNext": False,
            "hasPrevious": False
        }
    }
}
