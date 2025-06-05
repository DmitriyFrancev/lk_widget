from typing import Generator, Any


def filter_by_currency(transactions_list: list[dict], currency_name: str) -> Generator[dict, Any, None]:
    """
    Принимает список словарей, содержащих данные о транзакциях.
    Возвращает генератор словарей, значение ключа code у которых равняется параметру currency_name.
    """
    transaction_generator = (x for x in transactions_list if x.get('operationAmount', {})
    .get('currency', {}).get('code', 'No such element') == currency_name)
    return transaction_generator


def transaction_descriptions(transactions_list: list[dict]) -> Generator[str]:
    """
    Принимает список словарей, содержащих данные о транзакциях.
    Возвращает генератор значений ключа description.
    """
    description_generator = (description.get('description', 'No description') for description in transactions_list )
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


if __name__ == '__main__':

    test_dict_list = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
    {
        "id": 587085106,
        "state": "EXECUTED",
        "date": "2018-03-23T10:45:06.972075",
        "operationAmount": {
            "amount": "48223.05",
            "currency": {
                "name": "RUB",
                "code": "RUB"
            }
        },
        "description": "Открытие вклада",
        "to": "Счет 41421565395219882431"
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {
            "amount": "43318.34",
            "currency": {
                "name": "EUR",
                "code": "EUR"
            }
        },
        "description": "Перевод организации",
        "from": "Visa Classic 2842878893689012",
        "to": "Счет 35158586384610753655"
    },
    {
        "id": 214024827,
        "state": "CANCELED",
        "date": "2018-12-20T16:43:26.929246",
        "operationAmount": {
            "amount": "70946.18",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 10848359769870775355",
        "to": "Счет 21969751544412966366"
    }
    ]
    # result = filter_by_currency(test_dict_list, 'USD')
    # for i in range(5):
    #     print(next(result, 'No more transactions'))

    # tr_desc = transaction_descriptions(test_dict_list)
    # for i in range(5):
    #     print(next(tr_desc, 'No more transactions'))

    for card_number in card_number_generator():
        print(card_number)

    cards = card_number_generator(10, 12)
    print(next(cards, 'Значения закончились'))

