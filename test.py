import requests
import yaml
from datetime import datetime
from weather_class import Weather
import time
import pprint
ID = '7zvfpeHiJDPVSjpdexYbH'
SECRET = '8zBnVGL1yX1OIDpijkRO2lHl4yltmTR7ViiqwcWZ'
URL = 'https://data.api.xweather.com/conditions/'
# city_list = ['london,gb', 'paris,fr', 'tokyo,jp', 'berlin,de', 'brno,cz']
# with open('cities.yaml', 'w') as file:
#     yaml.dump(city_list, file)

# weather_list = []
# for city in city_list:
#     try:
#         r = requests.get(f'{URL}{city}?for=now&client_id={ID}&client_secret={SECRET}')
#         weather_list.append(r.json())
#     except Exception as e:
#         print(e)
# print(weather_list)
city_list = Weather.read_yaml()
# print(city_list)
weather_list = []
w1 = Weather()
# ww = w1.get_weather('london,gb')
for city in city_list:
    weather_list.append(w1.get_weather(city))
    time.sleep(3)

# pprint.pp(weather_list)
Weather.write_csv(weather_list)