import os
import jwt

SECRET_KEY = "some-very-long-string-of-random-characters-CHANGE-TO-YOUR-LIKING"

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
    "Name": "Joyce",
    "UserEmail": "admin@mrm.com",
  },
  "exp": 152664012
}

expired_token = jwt.encode(expired,SECRET_KEY)
token = jwt.encode(user, SECRET_KEY)
admin_token = jwt.encode(admin, SECRET_KEY)
fake_token = 'thisisa faketokem -adfoj903lamfa-30948rufjkflp94083920weosdk'