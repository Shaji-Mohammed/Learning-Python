"""
The test module for Vending Machine
"""

import pytest
import vending_machine as vendingMachine
from InsufficientFunds import InsufficientFunds

inserted_coins_list = []


def test_insert_coin():
    assert vendingMachine.insert_coin(5, inserted_coins_list) == [5]


def test_insert_invalid_coin():
    with pytest.raises(ValueError):
        assert vendingMachine.insert_coin(7, inserted_coins_list)


def test_buy_product():
    assert vendingMachine.buy_product("drink", 5) == (5 - 2.75)
    with pytest.raises(InsufficientFunds):
        assert vendingMachine.buy_product("chips", 2)


def test_return_change():
    assert vendingMachine.return_change(5) == [200, 200, 100]
    assert vendingMachine.return_change(10) == [200, 200, 200, 200, 200]
    assert vendingMachine.return_change(2.75) == [200, 25, 25, 25]
