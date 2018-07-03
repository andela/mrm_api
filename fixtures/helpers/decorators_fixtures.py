import os
import jwt

SECRET_KEY = os.getenv('SECRET_KEY')

null = None

user = {
  "UserInfo": {
    "name": "Samuel",
    "email": "user@mrm.com",
  }
}

admin = {
  "UserInfo": {
    "name": "Proxie",
    "email": "admin@mrm.com",
  }
}

expired = {
  "UserInfo": {
    "name": "Proxie",
    "email": "admin@mrm.com",
  },
  "exp": 152664012
}

room_mutation_query = '''
    mutation {
        createRoom(
          name: "Syne",
          calendarId: "id-w09e9slkj"
          roomType: "Meeting",
          capacity: 1,
          floorId: 1,
          imageUrl: "http://url.com",
          location:"Uganda") {
            room {
                name
                roomType
                capacity
                floorId,
                calendarId,
                imageUrl
                location
            }
        }
    }
'''

user_role_401_msg = b'{"errors":[{"message":"You are not authorized to perform this action","locations":[{"line":3,"column":9}]}],"data":{"createRoom":null}}'  # noqa: E501

query_string = '/mrm?query='+room_mutation_query

query_string_response = b'{"data":{"createRoom":{"room":{"name":"Syne","roomType":"Meeting","capacity":1,"floorId":1,"calendarId":"id-w09e9slkj","imageUrl":"http://url.com","location":"Uganda"}}}}'  # noqa: E501

expired_token = jwt.encode(expired, SECRET_KEY)

token = jwt.encode(user, SECRET_KEY)

admin_token = jwt.encode(admin, SECRET_KEY)

fake_token = 'thisisa faketokem -adfoj903lamfa-30948rufjkflp94083920weosdk'
