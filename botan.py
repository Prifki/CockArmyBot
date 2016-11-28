# utf-8

import requests
import json

TRACK_URL = 'https://api.botan.io/track'

def make_json(message):
    data = {}
    if message.from_user.username is not None:
        data['username'] = message.from_user.username
    if message.from_user.last_name is not None:
        data['last_name'] = message.from_user.last_name
    if message.from_user.first_name is not None:
        data['first_name'] = message.from_user.first_name
    return data


def track(token, uid, message, name='Message'):
    try:
        r = requests.post(
            TRACK_URL,
            params={"token": token, "uid": uid, "name": name},
            data=make_json(message),
            headers={'Content-type': 'application/json'}
        )
        return r.json()
    except requests.exceptions.Timeout:
        # set up for a retry, or continue in a retry loop
        return False
    except (requests.exceptions.RequestException, ValueError) as e:
        # catastrophic error
        print(e)
        return False