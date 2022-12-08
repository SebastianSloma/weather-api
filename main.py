import requests
import json


# https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

base_url = "https://api.openweathermap.org/data/2.5/weather?q="
api_key = "5d7318295595b8b58265b2035cfd6978"

city_name = input("Enter your City: ")

url = base_url + city_name + "&appid=" + api_key

response = requests.get(url)

data = response.json()

print(data)
