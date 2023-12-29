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
