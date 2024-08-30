def get_mask_card_number(card_number: int) -> str:
    """Функция маскировки номера банковской карты"""
    if type(card_number) != int:
        raise TypeError
    else:
        string_card_number = str(card_number)
        if len(string_card_number) != 16:
            raise ValueError
        else:
            return f"{string_card_number[0:4]} {string_card_number[4:6]}** **** {string_card_number[-4:]}"

def get_mask_account(account_number: int) -> str:
    """Функцию маскировки номера банковского счета"""
    if type(account_number) != int:
        raise TypeError
    else:
        string_account_number = str(account_number)
        if len(string_account_number) != 20:
            raise ValueError
        else:
            return f"**{string_account_number[-4:]}"
