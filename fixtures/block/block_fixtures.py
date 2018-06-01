
rooms_in_block_query = '''
    {
        getRoomsInABlock(blockId:1){
            name
            floors{
                name
                rooms{
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
                "floors": [
                    {
                        "name": "3rd",
                        "rooms": [
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
