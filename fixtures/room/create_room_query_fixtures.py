room_mutation_sample_string = '''
 mutation {
        createRoom(
          name: "Syne",
          calendarId: "andela.com_3836323338323230343935@resource.calendar.google.com",  # noqa: E501
          roomType: "Meeting",
          capacity: 1,
          locationId: %d,
          roomTags: [1],
          structureId: "b05fc5f2-b4aa-4f48-a8fb-30bdcc3fc968",
          imageUrl: "http://url.com",
          roomLabels: ["Epic tower", "1st Floor"]) {
            room {
                name
                roomType
                capacity
                locationId,
                calendarId,
                structureId,
                imageUrl
                roomTags {
                  name
                  color
                }
                roomLabels
            }
        }
    }
'''

room_mutation_query = room_mutation_sample_string % (1)

room_mutation_different_location_query = room_mutation_sample_string % (2)

room_invalid_calendar_id_mutation_query = '''
    mutation {
        createRoom(
            name: "Kigali", roomType: "Meeting", capacity: 6, locationId: 1,
            structureId: "b05fc5f2-b4aa-4f48-a8fb-30bdcc3fc968",
            calendarId:"andela.com_38363233383232303439@resource.calendar.google.com",
            imageUrl: "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg",
            roomLabels: ["Epic tower", "1st Floor"]) {  # noqa: E501
            room {
                name
            }
        }
    }
'''

rooms_query = '''
query {
  allRooms{
   rooms{
      name
      capacity
      roomType
      imageUrl
      roomTags {
          name
          color
      }
        }
    }
}
'''

invalid_room_label_query = '''
mutation {
  createRoom(
    name: "yaoundejsdcds",
    roomType: "Meeting",
    capacity: 4,
    locationId: 3,
    calendarId: "andela.com_3735303539313930363030@resource.calendar.google.com",
    structureId: "b05fc5f2-b4aa-4f48-a8fb-30bdcc3fc968",
    imageUrl: "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg", # noqa: E501
    roomLabels: ["{'id': '1', 'value': 'Office 1'}"]) {
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

non_existent_structure_room_label_query = '''
  mutation {
createRoom(name: "Djibouti", roomType: "Meeting", capacity: 4, locationId: 1,
structureId: "b05fc5f2-b4aa-4f48-a8fb-30bdcc3fc968",
calendarId:"andela.com_3334333830313238333634@resource.calendar.google.com",
imageUrl: "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg", # noqa: E501
roomLabels: ["Block Z", "10th Floor"]) {
    room {
      id
      name
      roomType
      capacity
      locationId
      imageUrl
      roomLabels
      roomTags {
        name
        color
      }

    }
  }
}
'''

db_rooms_query = '''
    {
    rooms{
                name
                capacity
                roomType
                imageUrl
                }
    }
    '''

room_mutation_query_duplicate_name = '''
    mutation {
        createRoom(
            name: "Entebbe", roomType: "Meeting", capacity: 4, locationId: 1,
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
                structureId
                imageUrl
                roomTags {
                  name
                  description
                }
            }
        }
    }
'''

room_duplicate_calender_id_mutation_query = '''
    mutation {
        createRoom(
            name: "Mbarara", roomType: "Meeting", capacity: 4, locationId: 1,
            calendarId:"andela.com_3630363835303531343031@resource.calendar.google.com",
            structureId: "b05fc5f2-b4aa-4f48-a8fb-30bdcc3fc968",
            imageUrl: "https://www.officelovin.com/wp-content/uploads/2016/10/andela-office-main-1.jpg",
            roomLabels: ["Epic tower", "1st Floor"]) {  # noqa: E501
            room {
                name
                roomType
                capacity
                imageUrl
            }
        }
    }
'''
