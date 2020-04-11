import requests
import json
import random
import pprint
import time

pp = pprint.PrettyPrinter(indent=2, width=160)


def load_data(filename=None, data=None):
  if filename:
    with open(filename, encoding="utf8") as file:
      data = json.loads(file.read())
  return data


def populate_data(url=None, payload=None, querystring=None, token=None):
    headers = {
        'Content-Type': 'application/json',
    }

    if token:
        headers['Authorization'] = token

    response = requests.request(
        method='POST',
        url=url,
        headers=headers,
        params=querystring,
        data=json.dumps(payload),
    )
    print(f'{response.status_code}:', response.json())

    return response.json()


if __name__ == '__main__':
    _url = 'http://localhost:3333'

    token_list = []
    for ong in load_data(filename='ongs.json'):
        ongs_url = f'{_url}/ongs'
        ong_id = populate_data(url=ongs_url, payload=ong, querystring=None)
        token_list.append(ong_id['id'])
        time.sleep(5)

    for data in load_data(filename='cases.json'):
        ongs_url = f'{_url}/incidents'
        auth_token = random.choice(token_list)
        populate_data(url=ongs_url, payload=data, querystring=None, token=auth_token)
        time.sleep(5)
