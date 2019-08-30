delete_user = '''
mutation {
    deleteUser(email: "new.user@andela.com") {
        user{
            id
            email
            location
            roles {
                id
                role
            }
        }
    }
}
'''

delete_user_2 = '''
mutation {
    deleteUser(email: "test.test@andela.com") {
        user{
            email
            roles {
                role
            }
        }
    }
}
'''

mutation_hard_delete_user = '''
mutation {
    deleteUser(email: "peter.adeoye@andela.com", remove: true) {
        user{
            email
            roles {
                role
            }
        }
    }
}
'''

expected_response_hard_delete_user = {
    "data": {
        "deleteUser": {
            "user": {
                "email": "peter.adeoye@andela.com",
                "roles": [
                    {
                        "role": "Admin"
                    }
                ]
            }
        }
    }
}

delete_self = '''
mutation {
    deleteUser(email: "peter.walugembe@andela.com") {
        user{
            id
            email
            location
            roles {
                id
                role
            }
        }
    }
}
'''

user_not_found = '''
mutation {
    deleteUser(email: "test@andela.com") {
        user{
            id
            email
            location
            roles {
                id
                role
            }
        }
    }
}
'''


expected_query_after_delete = {
    "data": {
        "deleteUser": {
            "user": {
                "email": "test.test@andela.com",
                "roles": [
                    {
                        "role": "Default User"
                    }
                ]
            }
        }
    }
}

expected_query_after_delete_for_admin = {
    "data": {
        "deleteUser": {
            "user": {
                "id": "2",
                "email": "new.user@andela.com",
                "roles": [
                    {
                        "id": "1",
                        "role": "Admin"
                    }
                ]
            }
        }
    }
}

user_invalid_email = '''
mutation {
    deleteUser(email: "userandelacom") {
        user{
            id
            email
            location
            roles {
                id
                role
            }
        }
    }
}
'''
