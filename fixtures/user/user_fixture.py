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

user_duplication_mutation_response = "mrm@andela.com User email already exists"

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
            "users": [
                {
                    "email": "peter.walugembe@andela.com"
                }
            ],
            "hasNext": True,
            "hasPrevious": False,
            "pages": 2
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
