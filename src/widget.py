from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card_account: str) -> str:
    """ Принимает строку содержащую название и номер карты/счета.
    Возвращает исходную строку со скрытым номером """

    final_string = ''
    just_number = ''
    just_alpha = ''

    for symbol in card_account:
        if symbol.isdigit():
            just_number += symbol
        elif symbol.isalpha() or symbol.isspace():
            just_alpha += symbol

    if len(just_number) == 16:
        final_string = just_alpha + get_mask_card_number(just_number)
    elif len(just_number) == 20:
        final_string = just_alpha + get_mask_account(just_number)

    return final_string


def get_date(date_string: str) -> str:
    """На вход получает строку вида '2024-03-11T02:26:18.671407'. Выводит дату в формате ДД.ММ.ГГГГ"""
    try:
        date_list = date_string[0:10].split('-')
        result_date = f'{date_list[2]}.{date_list[1]}.{date_list[0]}'
    except IndexError:
        return 'Некорректный формат даты'
    return result_date
