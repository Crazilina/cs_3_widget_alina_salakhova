import json
from datetime import datetime


def load_transactions(filename):
    """
    Загружает операции из файла JSON.
    """
    with open(filename, 'r') as file:
        return json.load(file)


def sort_transactions_by_date(transaction):
    """
    Возвращает дату операции для сортировки.
    """
    return datetime.strptime(transaction['date'], '%Y-%m-%dT%H:%M:%S.%f')


def get_last_five_executed(transactions):
    """
    Возвращает последние пять выполненных операций.
    """
    executed_transactions = [t for t in transactions if t.get('state') == 'EXECUTED']
    executed_transactions.sort(key=sort_transactions_by_date, reverse=True)
    return executed_transactions[:5]


def mask_card_info(info):
    """
    Маскирует номер карты или счета. Для номера карты оставляет видимыми первые 6 и последние 4 цифры.
    Для номера счета оставляет видимыми только последние 4 цифры.
    """
    if not info or len(info.split()) < 2:
        return info

    parts = info.split(' ')
    name = ' '.join(parts[:-1])
    number = ''.join(filter(str.isdigit, parts[-1]))

    # Проверяем, является ли номером карты или счетом
    if "Счет" in name or len(number) > 16 or 4 < len(number) < 16:
        return f"Счет **{number[-4:]}"
    elif len(number) == 16:
        return f"{name} {number[:4]} {number[4:6]}** **** {number[-4:]}"
    else:
        return info


