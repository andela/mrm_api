null = None
user_role_mutation_query = '''
mutation{
  createUsersRole(userId: 3, roleId: 1){
    userRole{
      roleId
      userId
    }
  }
}
'''

user_role_mutation_response = {
    "data": {
        "createUsersRole": {
            "userRole": {
                "roleId": 1,
                "userId": 3
            }
        }
    }
}

user_role_query = '''
query {
  usersRole {
    roleId
    userId
  }
}
'''

user_role_query_response = {
    "data": {
        "usersRole": [
            {
                "userId": 1,
                "roleId": 1
            },
            {
                "userId": 2,
                "roleId": 1
            },
            {
                "userId": 3,
                "roleId": 1
            }
        ]
    }
}

query_user_by_user_id = '''
query {
  userRole(userId: 1){
    userId
    roleId
  }
}
'''

query_user_by_user_id_response = {
    "data": {
        "userRole": {
            "userId": 1,
            "roleId": 1
        }
    }
}

change_user_role_mutation_query = '''
mutation{
  changeUserRole(email:"mrm@andela.com", roleId:1){
    user{
      email
      roles{
        id
      }
    }
  }
}
'''

change_user_role_mutation_response = {
    "data": {
        "changeUserRole": {
            "user": {
                "email": "mrm@andela.com",
                "roles": [
                    {
                        "id": "1"
                    }
                ]
            }
        }
    }
}

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
