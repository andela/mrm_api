null = None

send_invitation_template = '''
mutation{
    inviteToConverge(email: "%s"){
        email

    }
}
'''

query_user_by_name_template = '''
    query{
        userByName(userName:"%s"){
            name
            email
        }
    }
'''

change_user_location_template = '''
       mutation {
        changeUserLocation(email: "%s", locationId: %d) {
          user {
            name
            location
          }
        }
      }
   '''
set_user_location_template = '''
mutation {
  setUserLocation(locationId: %d){
    user{
      email
      location
    }
  }
}
'''

user_mutation_query = '''
mutation {
  createUser(email: "mrm@andela.com"
            name: "this user"
            location:"Lagos"
            picture: "www.andela.com/user"){
    user {
      email,
      name,
      picture,
      location
    }
  }
}
'''

user_query = '''
query {
    users{
      users{
         email,
      }
   }
}
'''

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
query_user_by_email = '''
 query {
  user(email: "peter.walugembe@andela.com"){
    email
  }
}
'''

change_user_role_mutation = '''
mutation{
    changeUserRole(email:"peter.walugembe@andela.com", roleId: 1){
        user{
            name
            roles{
                role
            }
        }
    }
}
'''

change_user_role_to_super_admin_mutation = '''
mutation{
    changeUserRole(email:"peter.walugembe@andela.com", roleId: 3){
        user{
            name
            roles{
                role
            }
        }
    }
}
'''

change_user_role_with_already_assigned_role_mutation = '''
mutation{
    changeUserRole(email:"peter.walugembe@andela.com", roleId: 1){
        user{
            name
            roles{
                role
            }
        }
    }
}
'''

change_user_role_to_non_existence_role_mutation = '''
mutation{
  createUserRole(userId: 1, roleId: 10){
    userRole{
      id
      roles{
        id
      }
    }
  }
}
'''

send_invitation_to_existent_user_query = send_invitation_template % (
    "peter.walugembe@andela.com"
)

send_invitation_to_nonexistent_user_query = send_invitation_template % (
    "beverly.kololi@andela.com"
)

send_invitation_to_invalid_email = send_invitation_template % (
    "peter.walugembe@gmail.com"
)

get_users_by_location = '''
query{
    users(page:1, perPage:1, locationId:2){
        users{
            name
            location
        }
    }
}
'''

get_users_by_location_and_role = '''
query{
    users(page:1, perPage:1, locationId:1, roleId:2){
        users{
            name
            location
        }
    }
}
'''

get_users_by_role = '''
query{
    users(page:1, perPage:1, roleId:1){
        users{
            name
            location
        }
    }
}
'''

change_role_of_non_existing_user_mutation = '''
mutation{
  changeUserRole(email:"someuser@andela.com", roleId:1){
    user{
      email
      roles{
        id
      }
    }
  }
}
'''

assign_role_to_non_existing_user_mutation = '''
mutation{
  createUserRole(userId: 100, roleId: 1){
    userRole{
      email
    }
  }
}
'''

filter_user_by_location = '''
query {
    users (locationId:5) {
      users {
        email
        name
        location }
    }
}
'''

query_user_by_name = query_user_by_name_template % ("Peter Adeoye")

query_non_existing_user_by_name = query_user_by_name_template % (
    "unknown user"
)

change_user_location_invalid_user_mutation = change_user_location_template % (
    "someinvaliduser@andela.com",
    1
)

change_user_location_invalid_location_id_mutation = change_user_location_template % (  # noqa: E501
    "peter.walugembe@andela.com",
    90
)

change_user_location_to_same_location_mutation = change_user_location_template % (  # noqa: E501
    "peter.walugembe@andela.com",
    1
)

change_user_location_valid_input_mutation = change_user_location_template % (
    "peter.walugembe@andela.com",
    2
)

set_user_location_mutation = set_user_location_template % (2)

set_user_location_exists_mutation = set_user_location_template % (1)
