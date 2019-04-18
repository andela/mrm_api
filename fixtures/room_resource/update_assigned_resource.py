null = None

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

expected_update_assigned_resource_query = {
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


non_existant_resource_id_query = '''
    mutation{
        updateAssignedResource(roomId:10, resourceId:10, quantity: 5){
            roomResource{
                roomId
                resourceId
                quantity
            }
        }
    }
'''

expected_non_existant_resource_id_query = {
  "errors": [
    {
      "message": "Invalid room or resource id",
      "locations": [
        {
          "line": 2,
          "column": 2
        }
      ],
      "path": [
        "updateAssignedResource"
      ]
    }
  ],
  "data": {
    "updateAssignedResource": null
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

expected_response_less_than_one_field = {
  "errors": [
    {
      "message": "Assigned quantity cannot be less than zero",
      "locations": [
        {
          "line": 2,
          "column": 2
        }
      ],
      "path": [
        "updateAssignedResource"
      ]
    }
  ],
  "data": {
    "updateAssignedResource": null
  }
}
