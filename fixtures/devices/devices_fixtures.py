null = None

query_devices = '''
        {
        allDevices{
            id
            resourceId
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
                                            "resourceId": 1,
                                            "lastSeen": "2018-06-08T11:17:58.785136",  # noqa: E501
                                            "dateAdded": "2018-06-08T11:17:58.785136",  # noqa: E501
                                            "name": "Samsung ",
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
                location:"Kenya",
                resourceId:1
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


update_device_query = '''
            mutation{
            updateDevice(
                deviceId:1
                name:"Apple tablet",
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

non_existant_id_response = {
                                "errors": [
                                    {
                                        "message": "DeviceId not found",
                                        "locations": [
                                            {
                                                "line": 3,
                                                "column": 13
                                                }
                                                ]
                                                }
                                                ],
                                "data": {
                                    "updateDevice": null
                                        }
                                        }
