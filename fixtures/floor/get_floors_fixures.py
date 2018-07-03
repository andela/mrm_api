get_all_floors_query = '''{
    allFloors {
        id
        name
        officeId
    }
}
'''

get_floors_query_response = {
    "data": {
        "allFloors": [
            {
                "id": "1",
                "name": "3rd",
                "officeId": 1
            }
        ]
    }
}
