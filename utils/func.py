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


def get_filtered(data):
    """
    Фильтрация списка, если значение state == executed
    :param data: данные
    :return: отфильтрованные данные по статусу операции - одобрена
    """
    data = [x for x in data if "state" in x and x["state"] == "EXECUTED"]
    return data


def get_last_date(data, count_lasts):
    """
    Сортировка данных по дате и получение последних пяти (или другого заданного количества)
    :param data: данные
    :param count_lasts: количество вывода данных
    :return: вывод последних 5 (или другого количества) операций
    """
    data = sorted(data, key=lambda x: x['data'], reverse=True)
    return data[:count_lasts]
