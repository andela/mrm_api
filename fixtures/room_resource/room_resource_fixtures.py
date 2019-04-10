resource_mutation_query = '''
    mutation {
        createResource(name: "Speakers", quantity: 3) {
            resource{
                name
                quantity
            }
        }
    }
'''

resource_mutation_response = {
    "data": {
        "createResource": {
            "resource": {
                "name": "Speakers",
                "quantity": 3
            }
        }
    }
}

resource_mutation_empty_name = '''
    mutation {
        createResource(name: "", quantity: 3) {
            resource{
                name
                quantity
            }
        }
    }
'''

resource_mutation_negative_quantity_query = '''
    mutation {
        createResource(name: "Speakers", quantity: -3) {
            resource{
                name
                quantity
            }
        }
    }
'''

resource_mutation_negative_quantity_response = \
    "The quantity should not be less than 0"
