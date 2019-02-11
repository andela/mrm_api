update_mutation = '''
    mutation{
  updateFirebaseToken(firebaseToken:"hakjacjihihaehcfkuqehihjfieq",roomId:1){
    room{
      firebaseToken
    }
  }
}
'''

update_response = {
  "data": {
    "updateFirebaseToken": {
      "room": {
        "firebaseToken": "hakjacjihihaehcfkuqehihjfieq"
      }
    }
  }
}

incorrect_room_id_mutation = '''
    mutation{
  updateFirebaseToken(firebaseToken:"hakjacjihihaehcfkuqehihjfieq",roomId:70){
    room{
      firebaseToken
    }
  }
}
'''

update_with_empty_token = '''
    mutation{
  updateFirebaseToken(firebaseToken:"",roomId:1){
    room{
      firebaseToken
    }
  }
}
'''
