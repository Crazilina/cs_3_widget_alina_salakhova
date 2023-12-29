from datetime import datetime
from src.utils import load_transactions, get_last_five_executed

TEST_JSON_FILE = 'src/operations.json'  # путь к файлу с банковскими данными


def convert_date(transaction):
    """ Помощник для преобразования даты из строки в объект datetime. """
    return datetime.strptime(transaction.get('date', '0001-01-01T00:00:00.000000'), '%Y-%m-%dT%H:%M:%S.%f')


def test_sort_transactions_by_date():
    """ Тестирование сортировки транзакций по дате. """
    transactions = load_transactions(TEST_JSON_FILE)
    executed_transactions = [t for t in transactions if t.get('state') == 'EXECUTED']
    sorted_transactions = sorted(executed_transactions, key=convert_date, reverse=True)
    last_five = get_last_five_executed(transactions)[:5]
    assert last_five == sorted_transactions[:5]
