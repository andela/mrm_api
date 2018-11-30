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
            id
            email
            roles {
                id
                role
            }
        }
    }
}
'''

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
                "id": "3",
                "email": "test.test@andela.com",
                "roles": [
                    {
                        "id": "2",
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
