resource_mutation_query = '''
    mutation {
        createResource(name: "Speakers") {
            resource{
                name
            }
        }
    }
'''

resource_mutation_response = {
    "data": {
        "createResource": {
            "resource": {
                "name": "Speakers"
            }
        }
    }
}

resource_mutation_empty_name = '''
    mutation {
        createResource(name: "") {
            resource{
                name
            }
        }
    }
'''
