from collections import OrderedDict

query_get_rooms_in_location = '''{
getRoomsInALocation(locationId:1){
    name
    capacity
    roomType
    imageUrl
    }
}
'''

expected_query_get_rooms_in_location = {'data': OrderedDict([('getRoomsInALocation', [OrderedDict([('name', 'Entebbe'), ('capacity', 6), ('roomType', 'meeting'), ('imageUrl', 'https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg')]), OrderedDict([('name', 'Tana'), ('capacity', 14), (  # noqa 501
    'roomType', 'meeting'), ('imageUrl', 'https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg')]), OrderedDict([('name', 'Buluma'), ('capacity', 10), ('roomType', 'meeting'), ('imageUrl', 'https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg')])])])}  # noqa 501
