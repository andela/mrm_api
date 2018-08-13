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
      users{
         email,
         location
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
          "location": "Kampala"
        },
        {
          "email": "mrm@andela.com",
          "location": "Lagos"
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
         location
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
      "users": [
        {
          "email": "peter.walugembe@andela.com",
          "location": "Kampala"
        }
      ],
      "hasNext": False,
      "hasPrevious": False,
      "pages": 1
    }
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
