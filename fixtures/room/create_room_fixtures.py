room_invalid_location_id_mutation = '''
    mutation {
        createRoom(
            name: "aso", roomType: "Meeting", capacity: 4,
            locationId: 9, roomTags: [1],
            calendarId:"andela.com_3836323338323230343935@resource.calendar.google.com",
            structureId: "b05fc5f2-b4aa-4f48-a8fb-30bdcc3fc968",
            imageUrl: "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg",
            roomLabels: ["Epic Tower", "1st Floor"]) {  # noqa: E501
            room {
                name
                roomType
                capacity
                imageUrl
                roomTags {
                    name
                    color
                    description
                }
            }
        }
    }
'''

room_invalid_tag_mutation = '''
    mutation {
        createRoom(
            name: "Mbarara", roomType: "Meeting", capacity: 4, roomTags: [8], locationId: 1,
            calendarId:"andela.com_3836323338323230343935@resource.calendar.google.com",
            structureId: "b05fc5f2-b4aa-4f48-a8fb-30bdcc3fc968",
            imageUrl: "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg",
            roomLabels: ["Epic tower", "1st Floor"]) {  # noqa: E501
            room {
                id
                name
                roomType
                capacity
                locationId
                imageUrl
            }
        }
    }
'''

room_name_empty_mutation = '''
    mutation {
        createRoom(
            name: "", roomType: "Meeting", capacity: 4,
            locationId: 1, roomTags: [1],
            calendarId:"andela.com_3836323338323230343935@resource.calendar.google.com",
            structureId: "b05fc5f2-b4aa-4f48-a8fb-30bdcc3fc968",
            imageUrl: "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg",
            roomLabels: ["Epic Tower", "1st Floor"]) {  # noqa: E501
            room {
                name
                roomType
                capacity
                imageUrl
            }
        }
    }
'''
