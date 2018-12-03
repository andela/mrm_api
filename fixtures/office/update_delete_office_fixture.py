null = None
update_office_with_wrong_ID_query = '''
    mutation {
        updateOffice(name: "The Crest", officeId:10 ) {
            office {
                name
                locationId
            }
        }
    }
'''

update_office_with_same_Name_query = '''
    mutation {
        updateOffice(name: "dojo", officeId:1 ) {
            office {
                name
                locationId
            }
        }
    }
'''
update_office_in_another_location_query = '''
    mutation {
        updateOffice(name: "The Crest", officeId:2 ) {
            office {
                name
                locationId
            }
        }
    }
'''

update_office_query = '''
    mutation {
        updateOffice(name: "Crest", officeId:1 ) {
            office {
                name
                locationId
            }
        }
    }
'''

office_mutation_response = {
    "data": {
        "updateOffice": {
            "office": {
                "name": "Crest",
                "locationId": 1,
            }
        }
    }
}

delete_office_mutation = '''
mutation{
    deleteOffice(officeId: 1){
        office{
            name
            blocks{
                name
                floors{
                    name
                    rooms{
                        name
                        roomType
                        capacity
                        resources{
                            name
                            quantity
                            devices{
                                name
                            }
                        }
                    }
                }
            }
        }
    }
}
'''

delete_office_mutation_response = {
    "data": {
        "deleteOffice": {
            "office": {
                "name": "St. Catherines",
                "blocks": [
                    {
                        "name": "Ec",
                        "floors": [
                            {
                                "name": "3rd",
                                "rooms": [
                                    {
                                        "name": "Entebbe",
                                        "roomType": "meeting",
                                        "capacity": 6,
                                        "resources": [
                                            {
                                                "name": "Markers",
                                                "quantity": 3,
                                                "devices": [
                                                    {
                                                        "name": "Samsung"
                                                    }
                                                ]
                                            }
                                        ]
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        }
    }
}

delete_non_existent_office_mutation = '''

mutation{
    deleteOffice(officeId: 10){
        office{
            name
        }
    }
}

'''

delete_unauthorised_location_mutation = '''
mutation{
    deleteOffice(officeId: 2){
        office{
            name
        }
    }
}
'''
