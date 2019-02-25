null = None

query_devices = '''
        {
        allDevices{
            id
            lastSeen
            dateAdded
            name
            location
        }
        }
        '''

expected_response_devices = {
                                "data": {
                                    "allDevices": [
                                        {
                                            "id": "1",
                                            "lastSeen": "2018-06-08T11:17:58.785136",  # noqa: E501
                                            "dateAdded": "2018-06-08T11:17:58.785136",  # noqa: E501
                                            "name": "Samsung",
                                            "location": "Nairobi"
                                            }
                                            ]
                                            }
                                            }


create_devices_query = '''
            mutation{
            createDevice(
                name:"Apple tablet",
                deviceType:"External Display",
                roomId:1,
                location:"Kenya",
            ){
                device{
                name
                location
                deviceType
                }
            }
            }
'''

expected_create_devices_response = {
                                    "data": {
                                            "createDevice": {
                                                "device": {
                                                    "name": "Apple tablet",
                                                    "location": "Kenya",
                                                    "deviceType": "External Display"  # noqa : E501
                                                    }
                                                    }
                                                    }
                                                    }

create_device_non_existant_room_id = '''
mutation{
            createDevice(
                name:"Apple tablet",
                deviceType:"External Display",
                roomId:4,
                location:"Kenya",
            ){
                device{
                name
                location
                deviceType
                }
            }
            }
            '''
expected_non_existant_room_response = '''
{
  "errors": [
    {
      "message": "Room not found",
      "locations": [
        {
          "line": 2,
          "column": 13
        }
      ],
      "path": [
        "createDevice"
      ]
    }
  ],
  "data": {
    "createDevice": null
  }
}
'''
update_device_query = '''
            mutation{
            updateDevice(
                deviceId:1
                name:"Apple tablet",
                roomId:1,
                deviceType:"External Display",
                location:"Kenya",
            ){
                device{
                name
                location
                deviceType
                }
            }
            }
'''


expected_update_device_response = {
                                    "data": {
                                        "updateDevice": {
                                            "device": {
                                                "name": "Apple tablet",
                                                "location": "Kenya",
                                                "deviceType": "External Display"
                                                }
                                                }
                                                }
                                                }


query_with_non_existant_id = '''
            mutation{
            updateDevice(
                deviceId:5
                name:"Apple tablet",
                roomId:1,
                deviceType:"External Display",
                location:"Kenya",
            ){
                device{
                name
                location
                deviceType
                }
            }
            }
'''

create_device_query_invalid_room = '''
            mutation{
            createDevice(
                name:"Apple tablet",
                deviceType:"External Display",
                roomId:6,
                location:"Kenya",
            ){
                device{
                name
                location
                deviceType
                }
            }
            }
'''

non_existant_id_response = "DeviceId not found"
devices_query = '/mrm?query='+create_devices_query
devices_query_response = b'{"data":{"createDevice":{"device":{"name":"Apple tablet","location":"Kenya","deviceType":"External Display"}}}}'# noqaE501
