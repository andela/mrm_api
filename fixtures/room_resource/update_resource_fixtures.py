from ..output.OutputBuilder import build
from ..output.Error import error_item

null = None

update_room_resource_query = '''
            mutation{
            updateRoomResource(resourceId:1,name:"Markers"){
                resource{
                name
                }
            }
            }
            '''

expected_update_room_resource_query = {
    "data": {
        "updateRoomResource": {
            "resource": {
                "name": "Markers"
            }
        }
    }
}


non_existant_resource_id_query = '''
                        mutation{
                        updateRoomResource(resourceId:6,name:"TV Screen"){
                            resource{
                            name
                            }
                        }
                        }
                        '''

ene_error = error_item
ene_error.message = "ResourceId not Found"
ene_error.locations = [{"line": 3, "column": 25}]
ene_data = {"updateRoomResource": null}
expected_non_existant_resource_id_query = build(
    error=ene_error.build_error(ene_error),
    data=ene_data
)

update_with_empty_field = '''
                    mutation{
                        updateRoomResource(resourceId:1,name:""){
                            resource{
                            name
                            }
                        }
                        }
'''

ere_error = error_item
ere_error.message = "name is required field"
ere_error.locations = [{"line": 3, "column": 25}]
ere_data = {"updateRoomResource": null}
expected_response_empty_field = build(
    error=ere_error.build_error(ere_error),
    data=ere_data
)
