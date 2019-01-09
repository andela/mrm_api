filter_by_block_query = '''query {
    filterByBlock(blockId: 1){
        id
        name
        blockId
        }
    }'''

filter_by_block_response = {
        "data": {
            "filterByBlock": [
                {
                    "id": "4",
                    "name": "3rd",
                    "blockId": 1
                }
            ]
        }
    }

filter_by_non_existent_block = '''query {
    filterByBlock(blockId: 8){
        id
        name
        blockId
        }
    }'''

error_response = {
        "errors": [
            {
                "message": "Floors not found in this block",
                "locations": [
                    {
                        "line": 2,
                        "column": 5
                    }
                ],
                "path": [
                    "filterByBlock"
                ]
            }
        ],
        "data": {
            "filterByBlock": None
        }
    }
