import requests


def weather_city(city: str):
    url = f'https://wttr.in/{city}?M?nTqu&lang=ru'
    response = requests.get(url)
    return response.text


print(weather_city('Череповец'),
      weather_city('Шереметьево'),
      weather_city('Лондон'))
