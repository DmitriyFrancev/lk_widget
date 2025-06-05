import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize('value, result', [
    ("7000792289606361", "7000 79** **** 6361"),
    ("1234abcd07922xzyr361", "1234 ab** **** 2xzy"),
    ("", "**** **  ")
])
def test_get_mask_card_number(value: str, result: str) -> None:
    assert get_mask_card_number(value) == result


@pytest.fixture
def account_number() -> str:
    return '73654108430135874305'


def test_get_mask_account(account_number: str) -> None:
    assert get_mask_account(account_number) == '**4305'


def test_get_mask_account_empty_number() -> None:
    assert get_mask_account('') == '**'
