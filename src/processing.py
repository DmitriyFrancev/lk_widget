def filter_by_state(income_list: list[dict], state: str = 'EXECUTED') -> str | list[dict]:
    """Возвращает список словарей, содержащих только те словари, у которых ключ state соответствует указанному
    значению (по умолчанию EXECUTED)"""
    output_list = []
    for dictionary in income_list:
        try:
            if dictionary['state'] == state:
                output_list.append(dictionary)
        except KeyError:
            return 'Отсутствует "state"'
    return output_list


def sort_by_date(income_list: list[dict], sorting_parameter: bool = True) -> list[dict]:
    """ Сортирует список словарей по значению ключа date. Сортировка производится по убыванию (по умолчанию)"""
    result_list = sorted(income_list, key=lambda item: item['date'], reverse=sorting_parameter)
    return result_list
