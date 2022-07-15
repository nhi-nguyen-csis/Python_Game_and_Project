'''

API source: https://openweathermap.org/api
'''
from Weather_API import *
import requests

# print(base_url, api_key)
city = input("Enter a city name: ")
request_url = f"{base_url}?appid={api_key}&q={city}"

# send the request to url
response = requests.get(request_url)

# check if response is successful
if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    fTemp = data['main']['temp']
    # convert fTemp to cTemp
    cTemp = round(fTemp - 273.15, 2)
    print(f"Weather: {weather}")
    print(f"Temperature: {cTemp} Celcius degree")
# if not successful
else:
    print("An error occured")
