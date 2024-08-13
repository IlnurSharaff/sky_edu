def get_mask_card_number(card_number: int) -> str:
    """Функция маскировки номера банковской карты"""
    string_card_number = str(card_number)
    return f"{string_card_number[0:4]} {string_card_number[5:7]}** **** {string_card_number[-4:]}"


def get_mask_account(account_number: int) -> str:
    """Функцию маскировки номера банковского счета"""
    string_account_number = str(account_number)
    return f"**{string_account_number[-4:]}"
