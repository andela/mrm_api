delete_user = '''
mutation {
    deleteUser(userId: 2) {
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

delete_self = '''
mutation {
    deleteUser(userId: 1) {
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
    deleteUser(userId: 8) {
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
                "id": "2",
                "email": "test.test@andela.com",
                "location": "Lagos",
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
