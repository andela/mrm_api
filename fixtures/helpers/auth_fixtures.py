import os
import jwt



user = {
  "UserInfo": {
    "name": "Joyce",
    "email": "user@mrm.com",
  }
}
no_user = {
  "UserInfo": {
    "name": "",
    "email": "",
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

expired_token = jwt.encode(expired)

token = jwt.encode(user)


admin_token = jwt.encode(admin)

fake_token = 'thisisa faketokem -adfoj903lamfa-30948rufjkflp94083920weosdk'
