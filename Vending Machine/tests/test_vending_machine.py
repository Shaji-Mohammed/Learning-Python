"""
The test module for Vending Machine
"""

import vendingMachine

inserted_coins_list = []


def test_insert_coin():
    assert vendingMachine.insert_coin(5, inserted_coins_list) == [5]
