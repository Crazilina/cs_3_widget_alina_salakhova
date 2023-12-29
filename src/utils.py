import json

def load_transactions(filename):
    """
    Загружает операции из файла JSON.
    """
    with open(filename, 'r') as file:
        return json.load(file)