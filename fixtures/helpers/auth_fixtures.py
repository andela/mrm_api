import os
import jwt

SECRET_KEY = os.getenv('SECRET_KEY')

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

token = jwt.encode(user, SECRET_KEY)

admin_token = jwt.encode(admin, SECRET_KEY)

fake_token = 'thisisa faketokem -adfoj903lamfa-30948rufjkflp94083920weosdk'
