import requests
import json
from helpers.auth import authentication
from api.user.models import User


def get_user_details(token, user_id):
    header = {"Authorization": 'Bearer ' + token}
    response = requests.get('https://api.andela.com/api/v1/users/' + user_id,
                            headers=header)
    info = response.content.decode('utf-8')
    data = json.loads(info)
    print('the data from the token is:::::::::::::::::::::::::::', data)
    user_data = {}
    user_data['email'] = data['email']
    user_data['name'] = data['name']
    user_data['picture'] = data['picture']
    user_data['location'] = data['location']['name']
    user_data['roles'] = data['roles'][1]['name']
    return user_data


def get_user_email_from_db():
    user_token = authentication.Auth.decode_token()
    user_email = user_token['email']
    user = User.query.filter_by(email=user_email).first()
    return user.email
