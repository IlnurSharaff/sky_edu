import pytest

from src.widget import mask_account_card, get_date

@pytest.mark.parametrize("income_data, expected_result", [('Maestro 1596837868705199', 'Maestro 1596 83** **** 5199'),
                                                          ('Счет 73654108430135874305', 'Счет **4305'),
                                                          ('Счет 64686473678894779589', 'Счет **9589'),
                                                          ('MasterCard 7158300734726758', 'MasterCard 7158 30** **** 6758'),
                                                          ('Счет 35383033474447895560', 'Счет **5560'),
                                                          ('Visa Classic 6831982476737658', 'Visa Classic 6831 98** **** 7658'),
                                                          ('Visa Platinum 8990922113665229', 'Visa Platinum 8990 92** **** 5229')
                                                          ])
def test_correct_data_mask_account_card(income_data, expected_result):
    assert mask_account_card(income_data) == expected_result

@pytest.mark.parametrize("income_data, expected_result", [('Maestro 441596837868705199', ValueError),
                                                          ('Счет 654108430135874305', ValueError),
                                                          (64686473678894779589, TypeError),
                                                          ('Счеты 35383033474447895560', ValueError),
                                                          ('', TypeError),
                                                          ])
def test_incorrect_data_mask_account_card(income_data, expected_result):
    with pytest.raises(expected_result):
        mask_account_card(income_data)

@pytest.mark.parametrize("income_data, expected_result", [('2024-03-11T02:26:18.671407', '11.03.2024'),
                                                          ('2022-04-01', '01.04.2022'),
                                                          ('2021-01-30 jgf jngfn jnfdjjh', '30.01.2021'),
                                                          ])
def test_correct_get_date(income_data, expected_result):
    assert get_date(income_data) == expected_result

@pytest.mark.parametrize("income_data, expected_result", [('', TypeError),
                                                          ('2022-04-', TypeError),
                                                          ('2021-13-30 jgf jngfn jnfdjjh', ValueError),
                                                          ('2021-02-30 jgf', ValueError),
                                                          ('2021-04-31 jgf jngfn jnfdjjh', ValueError),
                                                          ])
def test_incorrect_get_date(income_data, expected_result):
    with pytest.raises(expected_result):
        get_date(income_data)
