import json
import io
from datetime import date


def get_data_from_json(filename: str) -> list[dict]:
    """
    Данная функция считывает json файл и преобразует его в список словарей
    :param filename: путь до файла
    :return: список словарей
    """
    if type(filename) is not str:
        return []

    file = io.open(filename, encoding='utf-8')
    data = json.load(file)
    file.close()

    return data


def filter_data(operations_data: list[dict]) -> list[dict]:
    """
    Данная функция отфильтровывает основной массив и возвращает массив из выполненных операций
    :param operations_data: массив оъектов операций
    :return: отфильтрованный массив по выполненным операциям
    """
    if len(operations_data) == 0:
        return []
    res = []
    for data in operations_data:
        if data.get('state') == 'EXECUTED':
            res.append(data)

    return res


def string_to_date(date_str: str) -> object:
    """
    Эта функция фарматирует строку в объект даты в формате iso
    :param date_str: date_str
    :return: дату в формате iso
    """
    if date_str == "":
        return None
    sd = date_str.split("T")
    print(sd)
    if sd[0] == '' or len(sd) == 0:
        return None

    date_of_oper = sd[0]
    try:
        iso_date = date.fromisoformat(date_of_oper)
    except ValueError:
        return None

    return iso_date


