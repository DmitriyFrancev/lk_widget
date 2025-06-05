def get_mask_card_number(card_number: str) -> str:
    """
    Принимает номер карты. Возвращает номер карты в формате 0123 45** **** 2345.
    """
    masked_numbers = card_number[6:12]
    card_masked_numbers = card_number.replace(masked_numbers, "******")
    output_card_numbers = (
        f"{card_masked_numbers[0:4]} {card_masked_numbers[4:8]} "
        f"{card_masked_numbers[8:12]} {card_masked_numbers[12:16]}"
    )
    return output_card_numbers


def get_mask_account(account_number: str) -> str:
    """
    Принимает номер счета. Возвращает номер счета в формате **1234
    """
    output_account_number = f"**{account_number[-4:]}"
    return output_account_number
