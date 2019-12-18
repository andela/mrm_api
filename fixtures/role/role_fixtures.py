from ..output.OutputBuilder import build
from ..output.Error import error_item

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

rdm_error = error_item
rdm_error.message = "DevOps Role already exists"
rdm_error.locations = [{"line": 3, "column": 3}]
rdm_error.path = ["createRole"]
rdm_data = {"createRole": null}
role_duplication_mutation_response = build(
    error=rdm_error.build_error(rdm_error),
    data=rdm_data
)


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
                "role": "Test"
            },
            {
                "role": "Super Admin"
            },
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
