from ..output.OutputBuilder import build
from ..output.Error import error_item

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

nae_error = error_item
nae_error.message = "This email is not allowed"
nae_error.locations = [{"line": 3, "column": 3}]
nae_error.path = ["createUser"]
nae_data = {"createUser": null}
non_Andela_email_mutation_response = build(
    error=nae_error.build_error(nae_error),
    data=nae_data
)
