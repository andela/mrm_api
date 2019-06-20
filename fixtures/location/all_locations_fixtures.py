from collections import OrderedDict
all_locations_query = '''
{
    allLocations{
        name
        abbreviation
        rooms {
            name
            roomType
            capacity
            roomTags {
                name
                color
                description
            }
        }
    }
}
'''

expected_query_all_locations = {
    'data': OrderedDict([('allLocations',
                          [OrderedDict([('name', 'Kampala'), ('abbreviation', 'KLA'), ('rooms', [ # noqa 501
                              OrderedDict([('name', 'Buluma'), ('roomType', 'meeting'), # noqa 501
                                           ('capacity', 10), ('roomTags', [])]), # noqa 501
                              OrderedDict([('name', 'Entebbe'), ('roomType', 'meeting'), ('capacity', 6), ('roomTags', # noqa 501
                                                                                                           [OrderedDict([('name', 'Block-B'), ('color', 'green'), ('description', 'The description')])])]), # noqa 501
                              OrderedDict([('name', 'Tana'), ('roomType', 'meeting'), ('capacity', 14), ('roomTags', # noqa 501
                                                                                                         [OrderedDict([('name', 'Block-B'), ('color', 'green'), ('description', 'The description')])])])])]), # noqa 501
                              OrderedDict(
                              [('name', 'Lagos'), ('abbreviation', 'LOS'), ('rooms', [])]), # noqa 501
                              OrderedDict([('name', 'Nairobi'), ('abbreviation', 'NBO'), ('rooms', [])])])])} # noqa 501

pass_an_arg_all_locations = '''
    {
        allLocations(locationId: 1){
            name
            id
            abbreviation
        }
    }'''

expected_response_pass_an_arg = {'errors': [
    {'message': 'Unknown argument "locationId" on field "allLocations" of type "Query".', 'locations': [{'line': 3, 'column': 22}]}]} # noqa 501

all_location_no_hierachy = '''{
    allLocations{
        rooms {
            name
            roomType
            capacity
        }
    }
}'''

expected_all_location_no_hierachy = {'data': OrderedDict([('allLocations', [OrderedDict([('rooms', [OrderedDict([('name', 'Buluma'), ('roomType', 'meeting'), ('capacity', 10)]), OrderedDict( # noqa 501
    [('name', 'Entebbe'), ('roomType', 'meeting'), ('capacity', 6)]), OrderedDict([('name', 'Tana'), ('roomType', 'meeting'), ('capacity', 14)])])]), OrderedDict([('rooms', [])]), OrderedDict([('rooms', [])])])])} # noqa 501
