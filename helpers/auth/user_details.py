from helpers.auth import authentication
from api.user.models import User


def get_user_from_db():
    user_token = authentication.Auth.decode_token()
    user_email = user_token['email']
    user = User.query.filter_by(email=user_email).first()
    return user
