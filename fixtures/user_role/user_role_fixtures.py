null = None
user_role_mutation_query = '''
mutation{
  createUserRole(userId: 3, roleId: 1){
    userRole{
      id
      roles{
        id
      }
    }
  }
}
'''

user_mutation_query_for_duplicated_role = '''
mutation{
  createUserRole(userId: 1, roleId: 1){
    userRole{
      id
      roles{
        id
      }
    }
  }
}
'''

user_role_mutation_response = {
    "data": {
        "createUserRole": {
            "userRole": {
                "id": "3",
                "roles": [
                    {
                        "id": "1"
                    }
                ]
            }
        }
    }
}

user_role_query = '''
query{
  users{
    users{
      id
      roles{
        role
      }
    }
  }
}
'''

user_role_query_response = {
    "data": {
        "users": {
            "users": [
                {
                    "id": "3",
                    "roles": [
                        {
                            "role": "Default"
                        }
                    ]
                },
                {
                    "id": "2",
                    "roles": [
                        {
                            "role": "Admin"
                        }
                    ]
                },
                {
                    "id": "1",
                    "roles": [
                        {
                            "role": "Admin"
                        }
                    ]
                },

            ]
        }
    }
}

query_users_by_user_role = '''
query {
  users(roleId:1){
    users{
      roles
      {
        role
      }
    }
  }
}
'''

query_users_by_user_role_response = {
    "data": {
        "users": {
            "users": [
              {
                "roles": [
                    {
                        "role": "Admin"
                    }
                ]
              },
              {
                "roles": [
                    {
                        "role": "Admin"
                    }
                ]
              }
            ]
        }
    }
}

change_user_role_mutation_query = '''
mutation{
  changeUserRole(email:"mrmtestuser@andela.com", roleId:1){
    user{
      email
      roles{
        id
      }
    }
  }
}
'''

change_user_role_mutation_response = "Role changed but email not sent"

change_unavailable_user_role_mutation_query = '''
mutation{
  changeUserRole(email:"someemail@andela.com", roleId:1){
    user{
      email
      roles{
        id
      }
    }
  }
}
'''

change_unavailable_user_role_mutation_response = {
    "errors": [
        {
            "message": "User not found",
            "locations": [
                {
                    "line": 3,
                    "column": 3
                }
            ],
            "path": [
                "changeUserRole"
            ]
        }
    ],
    "data": {
        "changeUserRole": null
    }
}

assign_invalid_user_role_mutation = '''
mutation{
  changeUserRole(email:"mrm@andela.com", roleId:10){
    user{
      email
      roles{
        id
      }
    }
  }
}
'''

assign_invalid_user_role_response = {
    "errors": [
        {
            "message": "invalid role id",
            "locations": [
                {
                    "line": 3,
                    "column": 3
                }
            ],
            "path": [
                "changeUserRole"
            ]
        }
    ],
    "data": {
        "changeUserRole": null
    }
}
