from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(user_info: str) -> str:
    """обработка информации о картах и счетах"""
    if type(user_info) != str:
        raise TypeError
    user_info_list = list(user_info.split())
    if len(user_info_list) < 2:
        raise TypeError
    else:
        if user_info_list[0] == "Счет":
            user_info_list[-1] = get_mask_account(int(user_info_list[-1]))
        else:
            user_info_list[-1] = get_mask_card_number(int(user_info_list[-1]))
        return " ".join(str(element) for element in user_info_list)


def get_date(date_info: str) -> str:
    """возврат даты в формате ДД.ММ.ГГГГ"""
    if type(date_info) != str:
        raise TypeError
    if len(date_info) < 10 or type(int(date_info[8:10])) != int or type(int(date_info[5:7])) != int or type(int(date_info[0:4])) != int:
        raise TypeError
    if int(date_info[5:7]) > 12:
        raise ValueError
    if int(date_info[5:7]) in (1, 3, 5, 7, 8, 10, 12):
        if int(date_info[8:10]) > 31:
            raise ValueError
    if int(date_info[5:7]) in (4, 6, 9, 11):
        if int(date_info[8:10]) > 30:
            raise ValueError
    if int(date_info[5:7]) == 2:
        if int(date_info[0:4]) % 4 == 0:
            if int(date_info[8:10]) > 29:
                raise ValueError
        else:
            if int(date_info[8:10]) > 28:
                raise ValueError
    return f"{date_info[8:10]}.{date_info[5:7]}.{date_info[0:4]}"
