
rooms_in_block_query = '''
    {
        getRoomsInABlock(blockId:1){
            name
            floor{
                name
                room{
                    name
                    capacity
                    roomType
                }
            }
        }
    }
'''


rooms_in_block_query_response = {
    "data": {
        "getRoomsInABlock": [
            {
                "name": "EC",
                "floor": [
                    {
                        "name": "3rd",
                        "room": [
                            {
                                "name": "Entebbe",
                                "capacity": 6,
                                "roomType": "meeting"
                            }
                        ]
                    }
                ]
            }
        ]
    }
}
