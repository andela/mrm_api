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
  user(email: "mrm@andela.com"){
    email
  }
}
'''

query_user_email_response = {
    "data": {
        "user": {
            "email": "mrm@andela.com",
        }
    }
}

change_user_role_mutation = '''
mutation{
    changeUserRole(email:"mrmtestuser@andela.com", roleId: 1){
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
