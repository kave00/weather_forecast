import pandas as pd
from datetime import datetime
import requests
import yaml
import sys
sys.path.append("..")
from config.global_config import *


class Weather:
    @staticmethod
    def read_yaml():
        with open(r'config/cities.yaml') as file:
            city_list = yaml.load(file, Loader=yaml.FullLoader)
            return city_list
    def get_weather(self, city):
        w_dict = {}
        try:
            r = requests.get(f'{URL}{city}?for=now&client_id={ID}&client_secret={SECRET}')
            result = r.json().get('response')[0].get('periods')[0]
            w_dict['city'] = city
            w_dict['time'] = datetime.now().strftime('%Y-%m-%d, %H:%M:%S')
            w_dict['temperature'] = result.get('tempC')
            return w_dict
        except Exception as e:
            print(e)
    @staticmethod
    def write_csv(info: list):
        df = pd.DataFrame(info)
        df.to_csv('weather.csv', index=False)




