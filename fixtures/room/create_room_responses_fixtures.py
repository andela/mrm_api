from ..output.OutputBuilder import build
from ..output.Error import error_item

null = None

room_mutation_query_response = {'data': {'createRoom': {
    'room': {
        'name': 'Syne',
        'roomType': 'Meeting',
        'capacity': 1,
        'locationId': 1,
        'calendarId': 'andela.com_3836323338323230343935@resource.calendar.google.com',   # noqa: E501
        'structureId': "b05fc5f2-b4aa-4f48-a8fb-30bdcc3fc968",
        'imageUrl': 'http://url.com',
        'roomTags': [{'name': 'Block-B', 'color': 'green'}],
        'roomLabels': ['Epic tower', '1st Floor']
    }
}
}
}

room_mutation_response = {
    "data": {
        "createRoom": {
            "room": {
                "name": "Mbarara",
                "roomType": "Meeting",
                "capacity": 4,
                "imageUrl": "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg"  # noqa: E501
            }
        }
    }
}

ric_error = error_item
ric_error.message = "Room calendar Id is invalid"
ric_error.locations = [{'line': 3, 'column': 9}]
ric_error.path = ['createRoom']
ric_data = {'createRoom': null}
room_invalid_calendar_id_mutation_response = build(
    ric_error.build_error(ric_error),
    ric_data
)
db_rooms_query_data = {
        "rooms": [
            {
                "name": "Entebbe",
                "capacity": 6,
                "roomType": "meeting",
                "imageUrl": "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg"  # noqa: E501
            },
            {
                "name": "Tana",
                "capacity": 14,
                "roomType": "meeting",
                "imageUrl": "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg"  # noqa: E501
            }
        ]
    }
db_rooms_query_response = build(
    data=db_rooms_query_data
)

query_rooms_response = {
    "data": {
        "allRooms": {
            "rooms": [
                {
                    "name": "Entebbe",
                    "capacity": 6,
                    "roomType": "meeting",
                    "roomTags": [
                        {
                            "name": "Block-B",
                            "color": "green"
                        }
                    ],
                    "imageUrl": "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg"  # noqa: E501
                },
                {
                    "name": "Tana",
                    "capacity": 14,
                    "roomType": "meeting",
                    "roomTags": [
                        {
                            "name": "Block-B",
                            "color": "green"
                        }
                    ],
                    "imageUrl": "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg"  # noqa: E501
                }
            ]
        }
    }
}

rmq_error = error_item
rmq_error.message = "Entebbe Room already exists"
rmq_error.locations = [{'line': 3, 'column': 9}]
rmq_error.path = ['createRoom']
rmq_data = {'createRoom': null}
room_mutation_query_duplicate_name_response = build(
    rmq_error.build_error(rmq_error),
    rmq_data
)

rdc_error = error_item
rdc_error.message = "andela.com_3630363835303531343031@resource.calendar.google.com CalenderId already exists"  # noqa: E501
rdc_error.locations = [{'line': 3, 'column': 9}]
rdc_error.path = ['createRoom']
rdc_data = {'createRoom': null}
room_duplicate_calendar_id_mutation_response = build(
    rdc_error.build_error(rdc_error),
    rdc_data
)
