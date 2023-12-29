from datetime import datetime
from src.utils import load_transactions, get_last_five_executed, display_transaction

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


def test_get_last_five_executed():
    """ Тестирование получения последних пяти выполненных транзакций. """
    transactions = load_transactions(TEST_JSON_FILE)
    last_five = get_last_five_executed(transactions)
    assert len(last_five) <= 5
    assert all(transaction['state'] == 'EXECUTED' for transaction in last_five)
    for i in range(len(last_five) - 1):
        assert convert_date(last_five[i]) >= convert_date(last_five[i + 1])


def test_display_transaction():
    transaction = {
        "date": "2021-01-01T12:00:00.000000",
        "description": "Test Description",
        "from": "1234567890123456",
        "to": "Счет 987654321",
        "operationAmount": {
            "amount": "1000",
            "currency": {"name": "USD"}
        }
    }
    output = display_transaction(transaction)
    expected_output = "01.01.2021 Test Description\n1234567890123456 -> Счет **4321\n1000 USD\n"
    assert output == expected_output

