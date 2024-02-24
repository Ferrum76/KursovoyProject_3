from datetime import date
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
    Эта функция фильтрует основной массив и возвращает массив выполненных операций
    :param operations_data: массив объектов операций
    :return: отфильтрованный массив выполненных операций
    """

    # Если входной массив пуст, возвращаем пустой массив
    if len(operations_data) == 0:
        return []

    # Создаем пустой массив для результатов
    res = []

    # Проходим по всем объектам во входном массиве
    for data in operations_data:
        # Если состояние объекта равно 'EXECUTED', добавляем его в результаты
        if data.get('state') == 'EXECUTED':
            res.append(data)

    # Возвращаем массив выполненных операций
    return res


def string_to_date(date_str: str) -> date | None:
    """
    Эта функция фарматирует строку в объект даты в формате iso
    :param date_str: date_str
    :return: дату в формате iso или None, если формат строки некорректен
    """
    # Если строка пустая, возвращаем None
    if date_str == "":
        return None

    # Разбиваем строку на две части по символу "T"
    sd = date_str.split("T")
    # Если первая часть пустая или разделение не произошло, возвращаем None
    if sd[0] == '' or len(sd) == 0:
        return None

    # Сохраняем дату операции
    date_of_oper = sd[0]
    try:
        # Пытаемся преобразовать дату в формат iso
        iso_date = date.fromisoformat(date_of_oper)
    except ValueError:
        # Если преобразование не удалось, возвращаем None
        return None

    # Возвращаем преобразованную дату
    return iso_date


def get_last_five_data(data: list[dict]) -> list[dict]:
    last_data = sorted(data, key=lambda x: string_to_date(x["date"]), reverse=True)

    return last_data[:5]


def parse_date(date_str: str) -> str:
    """
    Эта функция преобразует строку в объект даты в формате iso.
    :param date_str: входная строка с датой.
    :return: дату в формате 'дд.мм.гггг' или пустую строку, если входная строка не может быть обработана.
    """
    # Если входная строка пуста, возвращаем пустую строку
    if date_str == "":
        return ""

    # Разделяем входную строку на две части: дату и время
    sd = date_str.split("T")
    # Если дата отсутствует или входная строка пуста, возвращаем пустую строку
    if sd[0] == '' or len(sd) == 0:
        return ""

    # Получаем дату операции
    date_of_oper = sd[0]
    try:
        # Пытаемся преобразовать строку с датой в объект даты
        iso_date = date.fromisoformat(date_of_oper)
    except ValueError:
        # Если преобразование не удалось, возвращаем пустую строку
        return ""

    # Возвращаем дату в формате 'дд.мм.гггг'
    return iso_date.strftime('%d.%m.%Y')
