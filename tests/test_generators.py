import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


# Фикстуры для проверки функций-генераторов, содержащие:
# - тестовый список словарей с данными о транзакциях
# - пустой тестовый список словарей
@pytest.fixture
def test_list_dicts() -> list[dict]:
    test_list_data = [
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
    return test_list_data


@pytest.fixture
def empty_list() -> list[dict]:
    return [{}]


# Проверка на тестовом списке словарей
def test_filter_by_currency(test_list_dicts: list[dict]) -> None:
    expected_result = [
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572',
         'operationAmount': {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод организации', 'from': 'Счет 75106830613657916952',
         'to': 'Счет 11776614605963066702'},
        {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878',
         'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542',
         'to': 'Счет 75651667383060284188'},
        {'id': 214024827, 'state': 'CANCELED', 'date': '2018-12-20T16:43:26.929246',
         'operationAmount': {'amount': '70946.18', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод организации', 'from': 'Счет 10848359769870775355',
         'to': 'Счет 21969751544412966366'}
    ]
    result = list(filter_by_currency(test_list_dicts, 'USD'))
    assert result == expected_result


# Проверка работы параметра currency_name
def test_filter_by_currency_eur(test_list_dicts: list[dict]) -> None:
    expected_result = [
        {
            'id': 873106923,
            'state': 'EXECUTED',
            'date': '2019-03-23T01:09:46.296404',
            'operationAmount': {
                'amount': '43318.34',
                'currency': {
                    'name': 'EUR',
                    'code': 'EUR'
                }
            },
            'description': 'Перевод организации',
            'from': 'Visa Classic 2842878893689012',
            'to': 'Счет 35158586384610753655'
        }
    ]
    result = list(filter_by_currency(test_list_dicts, 'EUR'))
    assert result == expected_result


# Проверка на пустом списке словарей
def test_empty_filtered_by_currency(empty_list: list[dict]) -> None:
    expected_result: list = []
    result = list(filter_by_currency(empty_list, 'USD'))
    assert result == expected_result


# Проверка на тестовом списке словарей
def test_transaction_description(test_list_dicts: list[dict]) -> None:
    expected_result = [
        'Перевод организации',
        'Открытие вклада',
        'Перевод со счета на счет',
        'Перевод организации',
        'Перевод организации'
    ]
    result = list(transaction_descriptions(test_list_dicts))
    assert result == expected_result


# Проверка на пустом списке словарей
def test_empty_transaction_descriptions(empty_list: list[dict]) -> None:
    expected_result = ['No description']
    result = list(transaction_descriptions(empty_list))
    assert result == expected_result


# Параметризация для проверки функции card_number_generator
@pytest.mark.parametrize('start_value, stop_value, result', [
    (1, 2, ['0000 0000 0000 0001', '0000 0000 0000 0002']),
    (2, 1, []),
    (9999999999999997, 9999999999999999, ['9999 9999 9999 9997', '9999 9999 9999 9998', '9999 9999 9999 9999'])
])
def test_card_number_generator(start_value: int, stop_value: int, result: list) -> None:
    assert list(card_number_generator(start_value, stop_value)) == result
