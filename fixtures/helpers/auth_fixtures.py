import os
import jwt

SECRET_KEY = os.getenv('SECRET_KEY')

user = {
  "UserInfo": {
    "name": "Joyce",
    "email": "user@mrm.com",
  }
}

admin = {
  "UserInfo": {
    "name": "Namuli",
    "email": "admin@mrm.com",
  }
}

expired = {
  "UserInfo": {
    "name": "Joyce",
    "email": "admin@mrm.com",
  },
  "exp": 152664012
}

expired_token = str(jwt.encode(expired, SECRET_KEY))

token = str(jwt.encode(user, SECRET_KEY))

admin_token = str(jwt.encode(admin, SECRET_KEY))

fake_token = "thisisa faketokem -adfoj903lamfa-30948rufjkflp94083920weosdk"
