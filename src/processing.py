def filter_by_state(income_list: list[dict], state: str = 'EXECUTED') -> list[dict]:
    """Возвращает список словарей, содержащих только те словари, у которых ключ state соответствует указанному
    значению (по умолчанию EXECUTED)"""
    output_list = []
    for dictionary in income_list:
        if dictionary['state'] == state:
            output_list.append(dictionary)
    return output_list


def sort_by_date(income_list: list[dict], sorting_parameter: bool = True) -> list[dict]:
    """ Сортирует список словарей по значению ключа date. Сортировка производится по убыванию (по умолчанию)"""
    result_list = sorted(income_list, key=lambda item: item['date'], reverse=sorting_parameter)
    return result_list


if __name__ == '__main__':
    test_list = [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                 {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
                 {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                 {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]

    # final = filter_by_state(test_list)
    # for i in final:
    #     print(i)
    #
    # final1 = filter_by_state(test_list, 'CANCELED')
    # for i in final1:
    #     print(i)
    #
    final3 = sort_by_date(test_list)
    for i in final3:
        print(i)
    print()
    final4 = sort_by_date(test_list, False)
    for i in final4:
        print(i)
