from ..output.OutputBuilder import build
from ..output.Error import error_item

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

dwm_error = error_item
dwm_error.message = "Naija Wing already exists"
dwm_error.locations = [{"line": 3, "column": 9}]
dwm_error.path = ["createWing"]
dwm_data = {"createWing": null}
duplicate_wing_mutation_response = build(
    error=dwm_error.build_error(dwm_error),
    data=dwm_data
)

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

wcn_error = error_item
wcn_error.message = "name is required field"
wcn_error.locations = [{"line": 3, "column": 9}]
wcn_error.path = ["createWing"]
wcn_data = {"createWing": null}
wing_creation_no_name_response = build(
    error=wcn_error.build_error(wcn_error),
    data=wcn_data
)

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

udw_error = error_item
udw_error.message = "Naija Wing already exists"
udw_error.locations = [{"line": 3, "column": 9}]
udw_error.path = ["updateWing"]
udw_data = {"updateWing": null}
update_duplicate_wing_mutation_response = build(
    error=udw_error.build_error(udw_error),
    data=udw_data
)

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

query_all_wings = '''
query{
  allWings {
    name
  }
}
'''

query_all_wings_response = {
    "data": {
        "allWings": [
                {"name": "Big Apple"},
                {"name": "Naija"}
            ]
    }
}
