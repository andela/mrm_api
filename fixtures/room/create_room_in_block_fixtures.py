

room_blockId_not_required_mutation = '''
    mutation {
        createRoom(
            name: "aso", roomType: "Meeting", capacity: 4, floorId: 1,
            blockId: 3
            officeId: 1
            calendarId:"andela.com_3836323338323230343935@resource.calendar.google.com",
            imageUrl: "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg") {  # noqa: E501
            room {
                name
                roomType
                capacity
                floorId
                imageUrl
            }
        }
    }
'''
