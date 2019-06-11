null = None

resource_query = '''
        {
            resourceByName(searchName: "Speakers") {
                name
                room {
                    room {
                        name
                    }
                    quantity
                }
            }
        }
    '''

blank_resource_query = '''
        {
            resourceByName(searchName: "") {
                name
                room {
                    room {
                        name
                    }
                    quantity
                }
            }
        }
    '''

resource_response = {
    "data": {
        "resourceByName": [
            {
                "name": "Speakers",
                "room": []
            }
        ]
    }
}

none_existing_resource_response = {
    "errors": [
        {
            "message": "No Matching Resource",
            "locations": [
                {
                    "line": 3,
                    "column": 13
                }
            ],
            "path": [
                "resourceByName"
            ]
        }
    ],
    "data": {
        "resourceByName": null
    }
}

search_blank_name_response = {
    "errors": [
        {
            "message": "Please input Resource Name",
            "locations": [
                {
                    "line": 3,
                    "column": 13
                }
            ],
            "path": [
                "resourceByName"
            ]
        }
    ],
    "data": {
        "resourceByName": null
    }
}
