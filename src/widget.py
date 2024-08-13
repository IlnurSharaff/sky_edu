from masks import get_mask_card_number, get_mask_account

def mask_account_card(user_info: str) -> str:
    """обработка информации о картах и счетах"""
    user_info_list = list(user_info.split())
    if user_info_list[0] == 'Счет':
        user_info_list[-1] = get_mask_account(user_info_list[-1])
    else:
        user_info_list[-1] = get_mask_card_number(user_info_list[-1])
    return " ".join(str(element) for element in user_info_list)

def get_date(date_info: str) -> str:
    """возврат даты в формате ДД.ММ.ГГГГ"""
    return f"{date_info[8:10]}.{date_info[5:7]}.{date_info[0:4]}"

