import requests


def check_weather_city(city: str):
    params = {'M':'','n':'','T':'','q':'','u':'','lang': 'ru'}
    url = f'https://wttr.in/{city}'
    response = requests.get(url=url,params=params)
    response.raise_for_status()
    return response.text




cities = ['Шереметьево', 'Череповец','Лондон']

for city in cities:
    print(check_weather_city(city))

