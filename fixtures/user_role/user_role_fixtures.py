user_role_mutation_query = '''
mutation{
  createUsersRole(userId: 1, roleId: 1){
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
        "userId": 1
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
