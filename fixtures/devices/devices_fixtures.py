from ..output.OutputBuilder import build
from ..output.Error import error_item

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

query_devices_with_filter = '''
        {
        allDevices(deviceLabels: "1st Floor"){
            id
            lastSeen
            dateAdded
            name
            location
        }
        }
        '''


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
een_error = error_item
een_error.message = "Device not found"
een_error.locations = [{"line": 3, "column": 9}]
een_error.path = ["specificDevice"]
een_data = {"specificDevice": null}
expected_error_non_existent_device_id = build(
    error=een_error.build_error(een_error),
    data=een_data
)

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

delete_device_mutation = '''
            mutation{
            deleteDevice(
                deviceId:1
            ){
                device{
                id
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

devices_query = '/mrm?query='+create_devices_query

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
