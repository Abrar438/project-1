import requests
from pprint import pprint

API _key = ''

city = input("Enter a city: ")

base_url = "https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid=" + API_Key + "&q=" + city

weather_data - requests.get(base_url).json()

pprint(weather_data)