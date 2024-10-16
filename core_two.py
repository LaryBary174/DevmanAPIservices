import requests
import os
from dotenv import load_dotenv


def shorten_link(token: str, url: str):
    urlAPI = 'https://api.vk.ru/method/utils.getShortLink'
    params = {'access_token': token, 'v': '5.199',
              'p1': 'v1',
              'url': url,
              'private': '0', }

    response = requests.post(url=urlAPI, params=params)
    response.raise_for_status()
    response_json = response.json()
    result = response_json['response']['short_url']
    return result


def count_clicks(token: str, short_url_key: str):
    urlAPI = 'https://api.vk.ru/method/utils.getLinkStats'
    params = {'access_token': token, 'v': '5.199',
              'p1': 'v1',
              'key': short_url_key,
              'interval': 'forever',
              'extended': '0', }
    response = requests.post(url=urlAPI, params=params)
    response.raise_for_status()
    result = response.json()
    return result['response']['stats']


def is_shorten_link(url):
    from urllib.parse import urlparse
    parse_url = urlparse(url)
    if parse_url.netloc == 'vk.cc' and parse_url.path != '':
        short_url_key = parse_url.path.lstrip('/')
        return short_url_key
    return False


def main():
    load_dotenv()
    token = os.getenv('TOKEN')
    url = input('Enter URL: ')
    short_url_key = is_shorten_link(url)
    try:
        if short_url_key:
            clicks_info = count_clicks(token, short_url_key)
            print('Инфа по кликам: ', clicks_info)
        else:
            short_link = shorten_link(token, url)
            print('Сокращенная ссылка: ', short_link)
    except Exception as e:
        print(f'Ошибка в переданном URL {e}')


if __name__ == '__main__':
    main()
