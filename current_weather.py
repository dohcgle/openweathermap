import requests
from pprint import pprint 

api_key = 'b406dcfbdc1728457a90d74456d40a54'
city_name = 'Tashkent'
url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'

r = requests.get(url)
data = r.json()

pprint(r.json())