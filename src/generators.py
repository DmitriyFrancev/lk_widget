from typing import Any, Generator


def filter_by_currency(transactions_list: list[dict], currency_name: str) -> Generator[dict, Any, None]:
    """
    Принимает список словарей, содержащих данные о транзакциях.
    Возвращает генератор словарей, значение ключа code у которых равняется параметру currency_name.
    """
    transaction_generator = (
        x for x in transactions_list if x.get('operationAmount', {})
        .get('currency', {}).get('code', 'No such element') == currency_name
    )
    return transaction_generator


def transaction_descriptions(transactions_list: list[dict]) -> Generator[str]:
    """
    Принимает список словарей, содержащих данные о транзакциях.
    Возвращает генератор значений ключа description.
    """
    description_generator = (description.get('description', 'No description') for description in transactions_list)
    return description_generator


def card_number_generator(start: int = 1, end: int = 2) -> Generator[str]:
    """
    Генерирует номера карт в формате 0000 0000 0000 0001 в заданном диапазоне.
    Принимает значения начального и конечного номеров диапазона
    """
    while start <= end:
        number = f'{(16 - len(str(start))) * '0'}{start}'
        card_num = f'{number[0:4]} {number[4:8]} {number[8:12]} {number[12:16]}'
        yield card_num
        start += 1
