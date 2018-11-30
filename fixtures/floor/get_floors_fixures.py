get_all_floors_query = '''{
    allFloors {
        id
        name
        blockId
    }
}
'''

get_floors_query_response = {
    "data": {
        "allFloors": [
            {
                "id": "1",
                "name": "3rd",
                "blockId": 1
            },
            {
                "id": "2",
                "name": "2nd",
                "blockId": 2
            }
        ]
    }
}
