filter_rooms_by_capacity = '''query {
  allRooms(capacity:6){
   rooms{
      name
      capacity
      roomType
      imageUrl
        }
    }
}
    '''
filter_rooms_by_location = '''query {
  allRooms(location:"Kampala"){
   rooms{
      name
      capacity
      roomType
      imageUrl
        }
    }
}
    '''
filter_rooms_by_wings_and_floors = '''
    query {
    allRooms(roomLabels:"1st Floor, Wing A") {
        rooms {
        id
        name
        roomLabels
        }
    }
    }
    '''

filter_rooms_by_non_existent_room_label = '''
    query {
    allRooms(roomLabels:"Random") {
        rooms {
        id
        name
        roomLabels
        }
    }
    }
    '''

filter_rooms_by_location_capacity = '''query {
  allRooms(location:"Kampala",capacity:6){
   rooms{
      name
      capacity
      roomType
      imageUrl
        }
    }
}
    '''
filter_rooms_by_tag = '''query {
    filterRoomsByTag(tagId: 1){
        id
        name
        }
    }'''

filter_rooms_by_tag_response = {
    "data": {
        "filterRoomsByTag": [
            {
                "id": "1",
                "name": "Entebbe"
            }
        ]
    }
}

filter_rooms_by_invalid_tag = '''query {
    filterRoomsByTag(tagId: 100){
        id
        name
        }
    }'''

filter_rooms_by_room_labels = '''query {
  allRooms(roomLabels:"Wing A"){
   rooms{
      name
      capacity
      roomType
      imageUrl
      roomLabels
        }
    }
}
    '''

filter_rooms_by_location_room_labels = '''query {
  allRooms(roomLabels:"Wing A", location:"Kampala"){
   rooms{
      name
      capacity
      roomType
      imageUrl
      roomLabels
        }
    }
}
    '''
filter_rooms_by_resource = '''query {
  allRooms(resources:"Markers"){
   rooms{
      name
      capacity
      roomType
      imageUrl
      roomLabels
        }
    }
}
    '''

filter_rooms_by_location_resource = '''query {
  allRooms(resources:"Markers", location:"Kampala"){
   rooms{
      name
      capacity
      roomType
      imageUrl
      roomLabels
        }
    }
}
    '''
