#! pip install requests

import requests
import json


def test(a, b):

    url = "https://faas-fra1-afec6ce7.doserverless.co/api/v1/web/fn-1f1056ff-de8e-4509-9811-27a68419f504/default/add"

    payload = '{"a":a, "b":b}'  # json
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, json=payload)

    print("salida", response)

    if 'result' not in json.loads(response.text):
        raise Exception('No hay result')

    return int(json.loads(response.text)['result'])



assert test(2, 2) == 3
assert test(2, 2) == 4
#print('STATUS:  ', response.status_code)
#print('RESPONSE:', response.text)