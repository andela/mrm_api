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

delete_device_response = {
    "data": {
        "deleteDevice": {
            "device": {
                "id": "1"
            }
        }
    }
}

non_existant_id_response = "DeviceId not found"

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

expected_response_devices_with_filter = {
    "data": {
        "allDevices": [
            {
                "dateAdded": "2018-06-08T11:17:58.785136",
                "id": "1",
                "lastSeen": "2018-06-08T11:17:58.785136",
                "location": "Kampala",
                "name": "Samsung"
            }
        ]
    }
}
