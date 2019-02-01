null = None
non_Andela_email_mutation = '''
mutation {
  createUser(email: "mrm@gmail.com"
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

non_Andela_email_mutation_response = {
    "errors": [
        {
            "message": "This email is not allowed",
            "locations": [
                {
                    "line": 3,
                    "column": 3
                }
            ],
            "path": [
                "createUser"
            ]
        }
    ],
    "data": {
        "createUser": null
    }
}
