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
                                            "location": "Kampala"
                                            }
                                            ]
                                            }
                                            }

query_device = '''
        {
        specificDevice(deviceId: 1){
            id
            lastSeen
            dateAdded
            name
            location
        }
        }
        '''

expected_response_device = {
    "data": {
        "specificDevice": {
            "id": "1",
            "lastSeen": "2018-06-08T11:17:58.785136",  # noqa: E501
            "dateAdded": "2018-06-08T11:17:58.785136",  # noqa: E501
            "name": "Samsung",
            "location": "Kampala"
            }
        }
    }

query_non_existent_device = '''
        {
        specificDevice(deviceId: 10000){
            id
            lastSeen
            dateAdded
            name
            location
        }
        }
        '''

expected_error_non_existent_device_id = {
    "errors": [
        {
            "message": "Device not found",
            "locations": [
                {
                    "line": 3,
                    "column": 9
                }
            ],
            "path": [
                "specificDevice"
            ]
        }
    ],
    "data": {
        "specificDevice": null
    }
    }

create_devices_query = '''
            mutation{
            createDevice(
                name:"Apple tablet",
                deviceType:"External Display",
                roomId:1
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
                                                    "location": "Kampala",
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
                roomId:4
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
                roomId:6
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
devices_query_response = b'{"data":{"createDevice":{"device":{"name":"Apple tablet","location":"Kenya","deviceType":"External Display"}}}}'  # noqaE501

search_device_by_name = '''
    query{
        deviceByName(deviceName:"Samsung"){
            id
            name
            deviceType
        }
    }
'''

search_non_existing_device = '''
    query{
        deviceByName(deviceName:"Apple"){
            id
            name
            deviceType
        }
    }
'''
search_non_existing_device_response = {'data': {'deviceByName': []}}

search_device_by_name_expected_response = {
    'data': {
        'deviceByName': [{
            'id': '1',
            'name': 'Samsung',
            'deviceType': 'External Display'
            }]
        }
    }
devices_query_response = b'{"data":{"createDevice":{"device":{"name":"Apple tablet","location":"Kampala","deviceType":"External Display"}}}}'  # noqaE501
