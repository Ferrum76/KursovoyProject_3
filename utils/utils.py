from datetime import date
import json
import io


def get_data_from_json(filename: str) -> list[dict]:
    """
    Данная функция считывает json файл и преобразует его в список словарей
    :param filename: путь до файла
    :return: список словарей
    """
    if not isinstance(filename, str):
        return []

    file = io.open(filename, encoding='utf-8')
    transactions = json.load(file)
    file.close()

    return transactions


def filter_data(transactions: list[dict]) -> list[dict]:
    """
    Эта функция фильтрует основной массив и возвращает массив выполненных операций
    :param operations_data: массив объектов операций
    :return: отфильтрованный массив выполненных операций
    """

    # Если входной массив пуст, возвращаем пустой массив
    if len(transactions) == 0:
        return []

    # Создаем пустой массив для результатов
    res = []

    # Проходим по всем объектам во входном массиве
    for transaction in transactions:
        # Если состояние объекта равно 'EXECUTED', добавляем его в результаты
        if transaction.get('state') == 'EXECUTED':
            res.append(transaction)

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


def get_last_five_data(transaction: list[dict]) -> list[dict]:
    last_data = sorted(
        transaction, key=lambda x: string_to_date(
            x["date"]), reverse=True)

    return last_data[:5]


def parse_date(date_str: str) -> str:
    """
    Эта функция преобразует строку в объект даты в формате iso.
    :param date_str: входная строка с датой.
    :return: дату в формате 'дд.мм.гггг' или пустую строку, если входная строка не может быть обработана.
    """
    # Пытаемся преобразовать дату в формат iso
    iso_date = string_to_date(date_str)

    # Если преобразование не удалось, возвращаем пустую строку
    if iso_date is None:
        return ""

    # Возвращаем дату в формате 'дд.мм.гггг'
    return iso_date.strftime('%d.%m.%Y')


def format_bank_info(bank_info: str) -> str:
    parts = bank_info.split()
    bank_digits = parts[-1]
    bank_name = " ".join(parts[:-1])

    if "Счет" in bank_name:
        return f"Счет **{bank_digits[-4:]}"
    else:
        return f"{bank_name} {bank_digits[0:4]} {
            bank_digits[4:6]}** **** {bank_digits[-4:]}"


def make_adr(transaction: dict) -> str:
    # Инициализируем переменные для хранения информации
    from_info = transaction.get('from', 'default')
    to_info = transaction.get('to', 'default')

    # Форматируем информацию о счетах
    if from_info != 'default' and from_info != '':
        from_info = format_bank_info(from_info)
    else:
        from_info = 'Счет отправителя неизвестен'

    if to_info != 'default' and to_info != '':
        to_info = format_bank_info(to_info)
    else:
        to_info = 'Счет получателя неизвестен'

    # Формируем строку
    res = f"{from_info} -> {to_info}"

    return res


def make_amount(transaction: dict) -> str:
    amount_info = transaction["operationAmount"]
    money_amount = amount_info["amount"]
    money_currency = amount_info["currency"]['name']

    result_str = f"{money_amount} {money_currency}"

    return result_str

def show_balance(transaction: dict) -> str:
    # Преобразование даты транзакции
    date = parse_date(transaction.get("date"))
    
    # Получение и форматирование описания транзакции
    description = transaction.get("description", "Описание транзакции отсутствует")
    
    # Форматирование информации об отправителе и получателе
    transaction_info = make_adr(transaction)
    
    # Форматирование суммы перевода и валюты
    amount = make_amount(transaction)
    
    # Сборка итоговой строки
    result = f"{date} {description}\n{transaction_info}\n{amount}"
    
    return result