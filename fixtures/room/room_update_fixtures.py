
null = None

query_update_all_fields = '''mutation{
                updateRoom(name:"Entebbe",newName:"Jinja",capacity:8,roomType:"board room"){
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
            updateRoom(name:"Entebbe",newName:"Jinja"){
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

query_without_keyword_name = '''mutation{
            updateRoom(newName:"Jinja"){
                room{
                    name
                    capacity
                    roomType
                    }
                }
                }
            '''

expected_query_without_keyword_name = {
             "errors": [
                    {
                    "message": "mutate() missing 1 required positional argument: 'name'",
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
                updateRoom(name:"Bakamoko",newName:"Jinja",capacity:8,roomType:"board room"){
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

