user_mutation_query = '''
mutation {
  createUser(email: "mrm@andela.com", location: "Lagos"){
    user {
      email,
      location
    }
  }
}
'''

user_mutation_response = {
  "data": {
    "createUser": {
      "user": {
        "email": "mrm@andela.com",
        "location": "Lagos"
      }
    }
  }
}

user_query = '''
query {
  users{
    email,
    location
  }
}
'''

user_query_response = {
  "data": {
    "users": [
      {
        "email": "patrick.walukagga@andela.com",
        "location": "Kampala"
      },
      {
        "email": "mrm@andela.com",
        "location": "Lagos"
      },
    ]
  }
}

query_user_by_email = '''
 query {
  user(email: "mrm@andela.com"){
    email,
    location
  }
}
'''

query_user_email_response = {
  "data": {
    "user": {
      "email": "mrm@andela.com",
      "location": "Lagos"
    }
  }
}
