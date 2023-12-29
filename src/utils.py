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