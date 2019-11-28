from ..output.OutputBuilder import build
from ..output.Error import error_item
from ..location.rooms_in_location_fixtures import rooms_sample

filter_rooms_by_capacity_response = {
    "data": {
        "allRooms": {
            "rooms": [
                {
                    "name": "Entebbe",
                    "capacity": 6,
                    "roomType": "meeting",
                    "imageUrl": "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg"  # noqa: E501
                }
            ]
        }
    }
}

filter_rooms_by_location_data = {
    "allRooms": {
        "rooms": rooms_sample
    }
}
filter_rooms_by_location_response = build(
    data=filter_rooms_by_location_data
)

filter_rooms_by_wings_and_floors_response = {
    'data': {
        'allRooms': {
            'rooms': [
                {
                    'id': '1',
                    'name': 'Entebbe',
                    'roomLabels': [
                        '1st Floor',
                        'Wing A'
                    ]
                }
            ]
        }
    }
}

filter_rooms_by_non_existent_room_label_response = {
    'data': {
        'allRooms': {
            'rooms': []
        }
    }
}

filter_rooms_by_location_capacity_response = {
    "data": {
        "allRooms": {
            "rooms": [
                {
                    "name": "Entebbe",
                    "capacity": 6,
                    "roomType": "meeting",
                    "imageUrl": "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg"  # noqa: E501
                }
            ]
        }
    }
}

filter_rooms_by_resources_capacity_response = {
    "data": {
        "allRooms": {
            "rooms": [
                {
                    "name": "Entebbe",
                    "capacity": 6,
                    "roomType": "meeting",
                    "imageUrl": "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg"  # noqa: E501
                }
            ]
        }
    }
}

frb_error = error_item
frb_error.message = "No rooms found with this tag"
frb_error.locations = [{'line': 2, 'column': 5}]
frb_error.path = ['filterRoomsByTag']
frb_data = {'filterRoomsByTag': None}
filter_rooms_by_invalid_tag_error_response = build(
    frb_error.build_error(frb_error),
    frb_data
)

filter_rooms_by_room_labels_response = {
    "data": {
        "allRooms": {
            "rooms": [
                {
                    "name": "Entebbe",
                    "capacity": 6,
                    "roomType": "meeting",
                    "imageUrl": "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg",  # noqa: E501
                    "roomLabels": ["1st Floor", "Wing A"]
                }
            ]
        }
    }
}
