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
                    "email": "peter.walugembe@andela.com",
                },
                {
                    "email": "peter.adeoye@andela.com"
                },
                {
                    "email": "mrm@andela.com",
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
                "email": "peter.walugembe@andela.com"
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

change_user_role_mutation_response = {
    "data": {
        "changeUserRole": {
            "user": {
                "name": "Peter Walugembe",
                "roles": [{
                    "role": "Admin"
                }]
            }
        }
    }
}

change_user_role_to_non_existence_role_mutation = '''
mutation{
    changeUserRole(email:"peter.walugembe@andela.com", roleId: 10){
        user{
            name
        }
    }
}
'''

change_user_role_to_non_existing_role_mutation_response = "Role id 10 does not exist"  # noqa: E501

send_invitation_to_existent_user_query = '''
mutation{
    inviteToConverge(email: "peter.walugembe@andela.com"){
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
