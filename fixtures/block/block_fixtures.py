get_all_blocks_query = '''{
    allBlocks {
        id
        name
    }
}
'''

get_blocks_query_response = {
    "data": {
        "allBlocks": [
            {
                "id": "1",
                "name": "EC"
            }
        ]
    }
}

rooms_in_block_query = '''
    {
        getRoomsInABlock(blockId:1){
            name
            capacity
            roomType
        }
    }
'''


rooms_in_block_query_response = {
    "data": {
        "getRoomsInABlock": [
            {
                "name": "Entebbe",
                "capacity": 6,
                "roomType": "meeting"
            }
        ]
    }
}
