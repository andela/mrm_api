
null = None

query_update_all_fields = '''mutation{
                updateRoom(id:1,name:"Jinja",capacity:8,roomType:"board room"){
                    room{
                        name
                        capacity
                        roomType
                        }
                    }
                    }
                '''

expected_query_update_all_fields = {
                
                "data": {
                    "updateRoom": {
                    "room": {
                        "name": "Jinja",
                        "capacity": 8,
                        "roomType": "board room"
                    }
                    }
                }
                }

query_update_only_required_field = '''mutation{
            updateRoom(id:1,name:"Jinja"){
                room{
                    name
                    capacity
                    roomType
                    }
                }
                }
            '''

expected_query_update_only_required_field = {
            "data": {
                "updateRoom": {
                "room": {
                    "name": "Jinja",
                    "capacity": 6,
                    "roomType": "meeting"
                }
                }
            }
            }

query_without_id = '''mutation{
            updateRoom(name:"Jinja"){
                room{
                    name
                    capacity
                    roomType
                    }
                }
                }
            '''

expected_query_without_id = {
             "errors": [
                    {
                    "message": "mutate() missing 1 required positional argument: 'id'",
                    "locations": [
                        {
                        "line": 2,
                        "column": 13
                        }
                    ]
                    }
                ],
                "data": {
                    "updateRoom": null
                }
        }


query_if_name_is_existant_room = '''mutation{
                updateRoom(id:4,name:"Jinja",capacity:8,roomType:"board room"){
                    room{
                    name
                    capacity
                    roomType
                    }
                }
                }
            '''

expected_query_if_name_is_existant_room = {
                "errors": [
                    {
                    "message": "'NoneType' object has no attribute 'name'",
                    "locations": [
                        {
                        "line": 2,
                        "column": 17
                        }
                    ]
                    }
                ],
                "data": {
                    "updateRoom": null
                }
                }

