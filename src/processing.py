def filter_by_state(base_list: list[dict], state: str = "EXECUTED") -> list[dict]:
    """возврат списка словарей по заданному значению ключа state"""
    filtered_list = []
    for dictionary in base_list:
        if dictionary["state"] == state:
            filtered_list.append(dictionary)
    return filtered_list


def sort_by_date(base_list: list[dict], sort_type: bool = True) -> list[dict]:
    """сортировка списка словарей по дате, по умолчанию - убывающий"""
    return sorted(base_list, key=lambda x: x["date"], reverse=sort_type)
