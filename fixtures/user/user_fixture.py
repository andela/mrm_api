null = None

user_mutation_query = '''
mutation {
  createUser(email: "mrm@andela.com"
            name: "this user"
            picture: "www.andela.com/user"){
    user {
      email,
      name,
      picture
    }
  }
}
'''

user_mutation_response = {
    "data": {
        "createUser": {
            "user": {
                "email": "mrm@andela.com",
                "name": "this user",
                "picture": "www.andela.com/user"
            }
        }
    }
}

user_duplication_mutation_response = {
    "errors": [{
        "message": "mrm@andela.com User email already exists",
        "locations": [{
            "line": 3,
            "column": 3
        }],
        "path": ["createUser"]
    }],
    "data": {
        "createUser": null
    }
}

user_query = '''
query {
    users{
      users{
         email,
      }
   }
}
'''

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

paginated_users_query = '''
query {
    users(page:1, perPage:1){
      users{
         email
      }
      hasNext
      hasPrevious
      pages
   }
}
'''

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

query_user_by_email = '''
 query {
  user(email: "peter.walugembe@andela.com"){
    email
  }
}
'''

query_user_email_response = {
    "data": {
        "user": {
            "email": "peter.walugembe@andela.com",
        }
    }
}

change_user_role_mutation = '''
mutation{
    changeUserRole(email:"peter.walugembe@andela.com", roleId: 1){
        user{
            name
            roles{
                role
            }
        }
    }
}
'''

change_user_role_to_super_admin_mutation = '''
mutation{
    changeUserRole(email:"peter.walugembe@andela.com", roleId: 3){
        user{
            name
            roles{
                role
            }
        }
    }
}
'''

change_user_role_mutation_response = "Role changed but email not sent"

change_user_role_with_already_assigned_role_mutation = '''
mutation{
    changeUserRole(email:"peter.walugembe@andela.com", roleId: 1){
        user{
            name
            roles{
                role
            }
        }
    }
}
'''

change_user_role_with_already_assigned_role_mutation_response = "This role is already assigned to this user"  # noqa: E501

change_user_role_to_non_existence_role_mutation = '''
mutation{
  createUserRole(userId: 1, roleId: 10){
    userRole{
      id
      roles{
        id
      }
    }
  }
}
'''

change_user_role_to_non_existing_role_mutation_response = "Role id does not exist"  # noqa: E501

send_invitation_to_existent_user_query = '''
mutation{
    inviteToConverge(email: "peter.walugembe@andela.com"){
        email

    }
}
'''

send_invitation_to_nonexistent_user_query = '''
mutation{
    inviteToConverge(email: "beverly.kololi@andela.com"){
        email
    }
}
'''

send_invitation_to_invalid_email = '''
mutation{
    inviteToConverge(email: "peter.walugembe@gmail.com"){
        email
    }
}
'''

send_invitation_to_existent_user_response = {
    "errors": [{
        "message": "User already joined Converge",
        "locations": [{
            "line": 3,
            "column": 5
        }],
        "path": ["inviteToConverge"]
    }],
    "data": {
        "inviteToConverge": null
    }
}

get_users_by_location = '''
query{
    users(page:1, perPage:1, locationId:2){
        users{
            name
            location
        }
    }
}
'''

get_users_by_location_and_role = '''
query{
    users(page:1, perPage:1, locationId:1, roleId:2){
        users{
            name
            location
        }
    }
}
'''

get_users_by_role = '''
query{
    users(page:1, perPage:1, roleId:1){
        users{
            name
            location
        }
    }
}
'''
get_user_by_role_reponse = {
    'data': {
        'users': {
            'users': [
                {
                    'name': 'Peter Adeoye',
                    'location': None
                }
            ]
        }
    }
}

change_role_of_non_existing_user_mutation = '''
mutation{
  changeUserRole(email:"someuser@andela.com", roleId:1){
    user{
      email
      roles{
        id
      }
    }
  }
}
'''

assign_role_to_non_existing_user_mutation = '''
mutation{
  createUserRole(userId: 100, roleId: 1){
    userRole{
      email
    }
  }
}
'''

filter_user_by_location = '''
query {
    users (locationId:5) {
      users {
        email
        name
        location }
    }
}
'''

query_user_by_name = '''
    query{
        userByName(userName:"Peter Adeoye"){
            name
            email
        }
    }
'''

query_user_by_name_response = {
    'data': {
        'userByName': [{
            'name': 'Peter Adeoye',
            'email': 'peter.adeoye@andela.com'
        }]
    }
}

query_non_existing_user_by_name = '''
    query{
        userByName(userName:"unknown user"){
            name
            email
        }
    }
'''

query_non_existing_user_by_name_response = {
    "errors": [
        {
            "message": "User not found",
            "locations": [
                {
                    "line": 3,
                    "column": 9
                }
            ],
            "path": [
                "userByName"
            ]
        }
    ],
    "data": {
        "userByName": null
    }
}

change_user_location_invalid_user_mutation = '''
       mutation {
        changeUserLocation(email: "someinvaliduser@andela.com", locationId: 1) {
          user {
            name
            location
          }
        }
      }
   '''


change_user_location_invalid_user_response = {
    "errors": [
        {
            "message": "User not found",
            "locations": [
                {
                    "line": 3,
                    "column": 9
                }
            ],
            "path": [
                "changeUserLocation"
            ]
        }
    ],
    "data": {
        "changeUserLocation": null
    }
}

change_user_location_invalid_location_id_mutation = '''
      mutation {
      changeUserLocation(email: "peter.walugembe@andela.com", locationId: 90) {
        user {
          name
          location
        }
      }
    }
  '''

change_user_location_invalid_location_id_response = {
    "errors": [
        {
            "message": "the location supplied does not exist",
            "locations": [
                {
                    "line": 3,
                    "column": 7
                }
            ],
            "path": [
                "changeUserLocation"
            ]
        }
    ],
    "data": {
        "changeUserLocation": null
    }
}

change_user_location_to_same_location_mutation = '''
       mutation {
        changeUserLocation(email: "peter.walugembe@andela.com", locationId: 1) {
          user {
            name
            location
          }
        }
      }
   '''

change_user_location_to_same_location_response = {
    "errors": [
        {
            "message": "user already in this location",
            "locations": [
                {
                    "line": 3,
                    "column": 9
                }
            ],
            "path": [
                "changeUserLocation"
            ]
        }
    ],
    "data": {
        "changeUserLocation": null
    }
}

change_user_location_valid_input_mutation = '''
       mutation {
        changeUserLocation(email: "peter.walugembe@andela.com", locationId: 2) {
          user {
            name
            location
          }
        }
      }
   '''

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

set_user_location_mutation = '''
mutation {
  setUserLocation(locationId: 2){
    user{
      email
      location
    }
  }
}
'''
set_user_location_exists_mutation = '''
mutation {
  setUserLocation(locationId: 1){
    user{
      email
      location
    }
  }
}
'''

set_user_location_exists_invalid_location = '''
mutation {
  setUserLocation(locationId: 10000){
    user{
      email
      location
    }
  }
}
'''

set_user_location_mutation_response = {
    "data": {
        "setUserLocation": {
            "user": {
                "email": "peter.adeoye@andela.com",
                "location": "Nairobi"
            }
        }
    }
}

set_location_for_user_with_location_response = {
    "errors": [
        {
            "message": "This user already has a location set.",
            "locations": [
                {
                    "line": 3,
                    "column": 3
                }
            ],
            "path": [
                "setUserLocation"
            ]
        }
    ],
    "data": {
        "setUserLocation": None
    }
}

set_user_location_exists_invalid_location_response = {
    "errors": [
        {
            "message": "The location supplied does not exist",
            "locations": [
                {
                    "line": 3,
                    "column": 3
                }
            ],
            "path": [
                "setUserLocation"
            ]
        }
    ],
    "data": {
        "setUserLocation": None
    }
}
