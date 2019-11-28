from ..output.OutputBuilder import build
from ..output.Error import error_item

null = None

delete_room_query = '''
                    mutation{
                    deleteRoom(roomId:1){
                    room{
                        name
                        capacity
                        roomType
                    }
                    }
                    }
                    '''

expected_response_room_query = {
    "data": {
        "deleteRoom": {
            "room": {
                "name": "Entebbe",
                "capacity": 6,
                "roomType": "meeting"
            }
        }
    }
}

delete_room_query_non_existant_room_id = '''
                    mutation{
                    deleteRoom(roomId:89){
                    room{
                        name
                        capacity
                        roomType
                    }
                    }
                    }
                    '''

ern_error = error_item
ern_error.message = "RoomId not found"
ern_error.locations = [{"line": 3, "column": 21}]
ern_data = {"deleteRoom": null}
expected_response_non_existant_room_id = build(
    error=ern_error.build_error(ern_error),
    data=ern_data
)
