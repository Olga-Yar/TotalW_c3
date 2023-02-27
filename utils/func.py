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


def get_filtered(data, filtered_empty_from=False):
    """
    Фильтрация списка, если значение state == executed
    :param filtered_empty_from: если в списке данных нет параметра from
    :param data: данные
    :return: отфильтрованные данные по статусу операции - одобрена
    """
    data = [x for x in data if "state" in x and x["state"] == "EXECUTED"]
    if filtered_empty_from:
        data = [x for x in data if 'from' in x]
    return data


def get_last_date(data, count_lasts):
    """
    Сортировка данных по дате и получение последних пяти (или другого заданного количества)
    :param data: данные
    :param count_lasts: количество вывода данных
    :return: вывод последних 5 (или другого количества) операций
    """
    data = sorted(data, key=lambda x: x['date'], reverse=True)
    return data[:count_lasts]


def get_formatted(data: json) -> list:
    """
    Возвращает отформатированный список
    :param data: данные
    :return: заданный формат вывода по операции
    """
    formatted_data = []
    for i in data:
        date = datetime.strptime(i["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        descriptions = i['description']

        if 'from' in i:
            from_ = i['from'].split()
            from_number = from_.pop(-1)
            from_number = f'{from_number[:4]} {from_number[4:6]}** **** {from_number[-4:]}'
            from_info = ' '.join(from_)
        else:
            from_number = ''
            from_info = 'Данные скрыты'

        to_ = f'**{i["to"][:4]}'
        amount = f'{i["operationAmount"]["amount"]} {i["operationAmount"]["currency"]["name"]}'
        formatted_data.append(f"""\
{date} {descriptions}
{from_info} {from_number} -> {to_}
{amount}
""")
        return formatted_data

