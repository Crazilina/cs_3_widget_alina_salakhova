import os
from utils import load_transactions, get_last_five_executed, display_transaction


def main():
    # Создаем абсолютный путь к файлу operations.json
    current_dir = os.path.dirname(os.path.abspath(__file__))
    json_file_path = os.path.join(current_dir, "operations.json")

    transactions = load_transactions(json_file_path)
    last_five_transactions = get_last_five_executed(transactions)
    for transaction in last_five_transactions:
        output = display_transaction(transaction)
        print(output)  # Печатаем возвращаемую строку
        print()  # Добавляем пустую строку между операциями


if __name__ == "__main__":
    main()
