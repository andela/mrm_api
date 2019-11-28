from ..output.OutputBuilder import build
from ..output.Error import error_item

null = None

user_mutation_response = {
    "data": {
        "createUser": {
            "user": {
                "email": "mrm@andela.com",
                "name": "this user",
                "picture": "www.andela.com/user",
                "location": "Lagos"
            }
        }
    }
}

udm_error = error_item
udm_error.message = "mrm@andela.com User email already exists"
udm_error.locations = [{"line": 3, "column": 3}]
udm_error.path = ["createUser"]
udm_data = {"createUser": null}
user_duplication_mutation_response = build(
    error=udm_error.build_error(udm_error),
    data=udm_data
)

user_query_response = {
    "data": {
        "users": {
            "users": [
                {
                    "email": "mrm@andela.com",
                },
                {
                    "email": "peter.adeoye@andela.com",
                },
                {
                    "email": "peter.walugembe@andela.com",
                },
            ]
        }
    }
}

paginated_users_response = {
    "data": {
        "users": {
            "users": [{
                "email": "peter.adeoye@andela.com"
            }],
            "hasNext": True,
            "hasPrevious": False,
            "pages": 3
        }
    }
}

query_user_email_response = {
    "data": {
        "user": {
            "email": "peter.walugembe@andela.com",
        }
    }
}

change_user_role_mutation_response = "Role changed but email not sent"

change_user_role_with_already_assigned_role_mutation_response = "This role is already assigned to this user"  # noqa: E501

change_user_role_to_non_existing_role_mutation_response = "Role id does not exist"  # noqa: E501

sit_error = error_item
sit_error.message = "User already joined Converge"
sit_error.locations = [{"line": 3, "column": 5}]
sit_error.path = ["inviteToConverge"]
sit_data = {"inviteToConverge": null}
send_invitation_to_existent_user_response = build(
    error=sit_error.build_error(sit_error),
    data=sit_data
)

get_user_by_role_reponse = {
    'data': {
        'users': {
            'users': [
                {
                    'name': 'Peter Adeoye',
                    'location': 'Lagos'
                }
            ]
        }
    }
}

query_user_by_name_response = {
    'data': {
        'userByName': [{
            'name': 'Peter Adeoye',
            'email': 'peter.adeoye@andela.com'
        }]
    }
}

qne_error = error_item
qne_error.message = "User not found"
qne_error.locations = [{"line": 3, "column": 9}]
qne_error.path = ["userByName"]
qne_data = {"userByName": null}
query_non_existing_user_by_name_response = build(
    error=qne_error.build_error(qne_error),
    data=qne_data
)

cul_error = error_item
cul_error.message = "User not found"
cul_error.locations = [{"line": 3, "column": 9}]
cul_error.path = ["changeUserLocation"]
cul_data = {"changeUserLocation": null}
change_user_location_invalid_user_response = build(
    error=cul_error.build_error(cul_error),
    data=cul_data
)

culi_error = error_item
culi_error.message = "the location supplied does not exist"
culi_error.locations = [{"line": 3, "column": 9}]
culi_error.path = ["changeUserLocation"]
culi_data = {"changeUserLocation": null}
change_user_location_invalid_location_id_response = build(
    error=culi_error.build_error(culi_error),
    data=culi_data
)

cult_error = error_item
cult_error.message = "user already in this location"
cult_error.locations = [{"line": 3, "column": 9}]
cult_error.path = ["changeUserLocation"]
cult_data = {"changeUserLocation": null}
change_user_location_to_same_location_response = build(
    error=cult_error.build_error(cult_error),
    data=cult_data
)

change_user_location_valid_input_response = {
    "data": {
        "changeUserLocation": {
            "user": {
                "name": "Peter Walugembe",
                "location": "Nairobi"
            }
        }
    }
}

sul_error = error_item
sul_error.message = "This user already has a location set."
sul_error.locations = [{"line": 3, "column": 3}]
sul_error.path = ["setUserLocation"]
sul_data = {"setUserLocation": null}
set_user_location_mutation_response = build(
    error=sul_error.build_error(sul_error),
    data=sul_data
)

slf_error = error_item
slf_error.message = "This user already has a location set."
slf_error.locations = [{"line": 3, "column": 3}]
slf_error.path = ["setUserLocation"]
slf_data = {"setUserLocation": null}
set_location_for_user_with_location_response = build(
    error=slf_error.build_error(slf_error),
    data=slf_data
)
