"""
The test module for Vending Machine
"""

import pytest
import vendingMachine

inserted_coins_list = []


def test_insert_coin():
    assert vendingMachine.insert_coin(5, inserted_coins_list) == [5]


def test_insert_invalid_coin():
    with pytest.raises(ValueError):
        assert vendingMachine.insert_coin(7, inserted_coins_list)

def test_buy_product():
    assert vendingMachine.buy_product("drink", 5) == (5 - 2.75)