import json
import io


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
