import pytest

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