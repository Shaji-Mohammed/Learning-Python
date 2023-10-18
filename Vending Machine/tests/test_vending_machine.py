"""
The test module for Vending Machine
"""

import pytest
import vending_machine as vendingMachine
from InsufficientFunds import InsufficientFunds


def test_insert_coin():
    inserted_coins_list = []
    assert vendingMachine.insert_coin_in_cents(5, inserted_coins_list) == 0.05


def test_insert_invalid_coin():
    inserted_coins_list = []
    with pytest.raises(ValueError):
        assert vendingMachine.insert_coin_in_cents(7, inserted_coins_list)


def test_buy_product():
    inserted_coins_list = []
    assert vendingMachine.buy_product("drink", 5) == [200, 25]
    with pytest.raises(InsufficientFunds):
        assert vendingMachine.buy_product("chips", 2)


def test_return_change():
    inserted_coins_list = []
    assert vendingMachine.return_change_in_cents(5) == [200, 200, 100]
    assert vendingMachine.return_change_in_cents(10) == [200, 200, 200, 200, 200]
    assert vendingMachine.return_change_in_cents(2.75) == [200, 25, 25, 25]

def test_run_chips():
    inserted_coins_list = []
    balance = vendingMachine.insert_coin_in_cents(200, inserted_coins_list)
    balance = vendingMachine.insert_coin_in_cents(100, inserted_coins_list)
    assert vendingMachine.buy_product("chips", balance) == [25, 25, 25]

def test_run_Drink():
    inserted_coins_list = []
    balance = vendingMachine.insert_coin_in_cents(200, inserted_coins_list)
    balance = vendingMachine.insert_coin_in_cents(100, inserted_coins_list)
    assert vendingMachine.buy_product("drink", balance) == [25]


def test_run_Candy():
    inserted_coins_list = []
    balance = vendingMachine.insert_coin_in_cents(200, inserted_coins_list)
    balance = vendingMachine.insert_coin_in_cents(25, inserted_coins_list)
    balance = vendingMachine.insert_coin_in_cents(100, inserted_coins_list)
    assert vendingMachine.buy_product("candy", balance) == [10]
