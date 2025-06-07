from typing import Generator


def filter_by_currency(transactions_list: list[dict], currency_name: str) -> Generator:
    """
    Принимает список словарей, содержащих данные о транзакциях.
    Возвращает генератор словарей, значение ключа code у которых равняется параметру currency_name.
    """
    for payment in transactions_list:
        if payment.get('operationAmount', {}).get('currency', {}).get('code', 'No such element') == currency_name:
            yield payment


def transaction_descriptions(transactions_list: list[dict]) -> Generator:
    """
    Принимает список словарей, содержащих данные о транзакциях.
    Возвращает генератор значений ключа description.
    """
    for payment in transactions_list:
        yield payment.get('description', 'No description')
    # yield (description.get('description', 'No description') for description in transactions_list)


def card_number_generator(start: int = 1, end: int = 2) -> Generator:
    """
    Генерирует номера карт в формате 0000 0000 0000 0001 в заданном диапазоне.
    Принимает значения начального и конечного номеров диапазона
    """
    while start <= end:
        number = f'{(16 - len(str(start))) * '0'}{start}'
        card_num = f'{number[0:4]} {number[4:8]} {number[8:12]} {number[12:16]}'
        yield card_num
        start += 1
