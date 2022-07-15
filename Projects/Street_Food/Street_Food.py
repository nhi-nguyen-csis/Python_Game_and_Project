'''

API source 1: https://documenter.getpostman.com/view/12204297/TVKJwEWL
API source 2: https://streetfoodapp.com/api
'''
import requests

base_url = 'http://data.streetfoodapp.com/1.1/'
request_url = f'{base_url}regions'

response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()

    idx = 1
    for restaurant in data:
        if restaurant['country'] == 'us':
            address = restaurant['example_location']['address']
            print(f"{idx}:\t{address}")
            idx += 1
else:
    print("Bad request! Error occurs")