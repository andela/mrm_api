user_mutation_query = '''
mutation {
  createUser(email: "mrm@andela.com"){
    user {
      email
    }
  }
}
'''

user_mutation_response = {
  "data": {
    "createUser": {
      "user": {
        "email": "mrm@andela.com"
      }
    }
  }
}

user_query = ''' 
query {
  users{
    email
  }
} 
'''

user_query_response = {
  "data": {
    "users": [
      {
        "email": "mrm@andela.com"
      }
    ]
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
      "email": "mrm@andela.com"
    }
  }
}

