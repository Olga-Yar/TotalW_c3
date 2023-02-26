import json
from datetime import datetime
import requests


def get_data(url):
    """
    Получение данных по ссылке, формат данных: json
    :param url: ссылка на данные
    :return: json файл
    """
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None, f'Ошибка при получении данных'
