import requests


def check_weather_city(city: str):
    params = {'M':'','n':'','T':'','q':'','u':'','lang': 'ru'}
    url = f'https://wttr.in/{city}'
    response = requests.get(url=url,params=params)
    response.raise_for_status()
    return response.text


def main(cities: list):
    for city in cities:
        print(check_weather_city(city))

cities = ['Шереметьево', 'Череповец','Лондон']

if __name__ == "__main__":
    main(cities)