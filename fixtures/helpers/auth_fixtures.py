import os
import jwt

SECRET_KEY = os.getenv('SECRET_KEY')

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

expired_token = jwt.encode(expired,SECRET_KEY)

token = jwt.encode(user, SECRET_KEY)
no_token=jwt.encode(no_user, SECRET_KEY)

admin_token = jwt.encode(admin, SECRET_KEY)

fake_token = 'thisisa faketokem -adfoj903lamfa-30948rufjkflp94083920weosdk'
true_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJVc2VySW5mbyI6eyJpZCI6Ii1MQ2NlT05mdi1Gbm44OG1nV3ZWIiwiZW1haWwiOiJkZW5uaXMuamphZ3dlQGFuZGVsYS5jb20iLCJmaXJzdF9uYW1lIjoiRGVubmlzIiwibGFzdF9uYW1lIjoiSmphZ3dlIiwibmFtZSI6IkRlbm5pcyBKamFnd2UiLCJwaWN0dXJlIjoiaHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tLy1uWjg0d2R0LW1vRS9BQUFBQUFBQUFBSS9BQUFBQUFBQUFBYy81TlN4endZa2ZOUS9waG90by5qcGc_c3o9NTAiLCJyb2xlcyI6eyJBbmRlbGFuIjoiLUtpaWhmWm9zZVFlcUM2YldUYXUiLCJUZWNobm9sb2d5IjoiLUtYSDdpTUU0ZWJNRVhBRWM3SFAifX0sImV4cCI6MTUyOTA2NjkxNH0.dGgUNmSCJ6Q1iaMzs4m4diKbhHCAmI4m0f_zxFFTE7y53pv9hwXOPCgN4_8MT_JcRdd6wY16rlJN5z5soxJK7lr3TLMal9VS9Dyx4Dlb_6BkSFCRgGmlJQaX_71Gi6uNayW_ucLAWrHOqf3Mcptj-5JaJzBMS_7xDnc5HA-V5BI'