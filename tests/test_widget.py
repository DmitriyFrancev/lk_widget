import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize('value, result', [
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("Счет 64686473678894779589", "Счет **9589"),
    ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
    ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353")
])

def test_mask_account_card(value, result):
    assert mask_account_card(value) == result


@pytest.mark.parametrize('value, result', [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2024", "Некорректный формат даты"),
    ("2025-03-11T02:26:18.671407.23149876", "11.03.2025"),
    ])

def test_get_date (value, result):
    assert get_date(value) == result
