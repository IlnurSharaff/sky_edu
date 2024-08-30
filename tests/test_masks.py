import pytest

from src.masks import get_mask_card_number, get_mask_account

@pytest.fixture
def card_mask_correct_number():
    return 7000792289606361

@pytest.fixture
def card_mask_correct_answer():
    return '7000 79** **** 6361'

@pytest.fixture
def card_mask_incorrect_number():
    return 47000792289606361

@pytest.fixture
def card_mask_account_correct_number():
    return 73654108430135874305

@pytest.fixture
def card_mask_account_correct_answer():
    return '**4305'

@pytest.fixture
def card_mask_account_incorrect_number():
    return 54108430135874305

def test_get_mask_card_number(card_mask_correct_number, card_mask_correct_answer, card_mask_incorrect_number):
    assert get_mask_card_number(card_mask_correct_number) == card_mask_correct_answer
    with pytest.raises(ValueError):
        get_mask_card_number(card_mask_incorrect_number)
    with pytest.raises(TypeError):
        get_mask_card_number()
    with pytest.raises(TypeError):
        get_mask_card_number('number')
    with pytest.raises(TypeError):
        get_mask_card_number('7000 7922 8960 6361')

def test_get_mask_account(card_mask_account_correct_number, card_mask_account_correct_answer, card_mask_account_incorrect_number):
    assert get_mask_account(card_mask_account_correct_number) == card_mask_account_correct_answer
    with pytest.raises(ValueError):
        get_mask_account(card_mask_account_incorrect_number)
    with pytest.raises(TypeError):
        get_mask_account()
    with pytest.raises(TypeError):
        get_mask_account('number')
    with pytest.raises(TypeError):
        get_mask_account('7000 7922 8960 6361')
