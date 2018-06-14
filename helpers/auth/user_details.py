import requests
import json


def get_user_details(token, user_id):
    cookies = {"jwt-token": token}
    response = requests.get('https://api.andela.com/api/v1/users/' + user_id,
                            cookies=cookies)
    info = response.content.decode('utf-8')
    data = json.loads(info)
    user_data = {}
    user_data['email'] = data['email']
    user_data['location'] = data['location']['name']
    user_data['roles'] = data['roles'][1]['name']
    return user_data
