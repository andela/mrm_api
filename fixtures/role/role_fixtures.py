null = None

role_mutation_query = '''
mutation {
  createRole(role:"DevOps"){
    role {
      role
    }
  }
}
'''

role_mutation_response = {
    "data": {
        "createRole": {
            "role": {
                "role": "DevOps"
            }
        }
    }
}

role_duplication_mutation_response = {
    "errors": [
        {
            "message": "DevOps Role already exists",
            "locations": [
                {
                    "line": 3,
                    "column": 3
                }
            ],
            "path": [
                "createRole"
            ]
        }
    ],
    "data": {
        "createRole": null
    }
}

role_query = '''
query {
  roles {
    role
  }
}
'''

role_query_response = {
    "data": {
        "roles": [
            {
                "role": "Admin"
            },
            {
                "role": "Ops"
            }
        ]
    }
}

query_role_by_role = '''
 query {
  role(role: "Ops"){
    role
  }
}
'''

query_role_by_role_response = {
    "data": {
        "role": {
            "role": "Ops"
        }
    }
}
