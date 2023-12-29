from utils import load_transactions, get_last_five_executed, display_transaction


def main():
    transactions = load_transactions('operations.json')
    last_five_transactions = get_last_five_executed(transactions)
    for transaction in last_five_transactions:
        output = display_transaction(transaction)
        print(output)  # Печатаем возвращаемую строку
        print()  # Добавляем пустую строку между операциями


if __name__ == "__main__":
    main()
