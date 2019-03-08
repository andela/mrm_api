
def map_remote_room_location_to_filter():
    '''
        map filters for room location
    '''
    return {
            'Nairobi': lambda remote_room: remote_room.startswith('Nairobi'),
            'Lagos': lambda remote_room: remote_room.find('ET-') != -1,
            'Kampala': lambda remote_room: remote_room.find('Kampala') != -1
            and not remote_room.startswith('Nairobi'),
            'all': lambda remote_room: True  # return True for all rooms
        }
