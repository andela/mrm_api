update_assigned_resource_query = '''
    mutation{
        updateAssignedResource(roomId:1, resourceId:1, quantity: 3){
            roomResource{
                roomId
                resourceId
                quantity
            }
        }
    }
'''

update_assigned_resource_query_response = {
  'data': {
    'updateAssignedResource': {
      'roomResource': {
        "roomId": "1",
        "resourceId": "1",
        'quantity': 3
      }
    }
  }
}

update_with_negative_quantity = '''
    mutation{
        updateAssignedResource(roomId:1, resourceId:1, quantity:-1 ){
        roomResource{
            roomId
            resourceId
            quantity
        }
    }
}
'''

update_non_existing_room = '''
  mutation{
        updateAssignedResource(roomId:11, resourceId:1, quantity:1 ){
        roomResource{
            roomId
            resourceId
            quantity
        }
    }
}
'''

update_non_existing_resource = '''
  mutation{
        updateAssignedResource(roomId:1, resourceId:12, quantity:1 ){
        roomResource{
            roomId
            resourceId
            quantity
        }
    }
}
'''
