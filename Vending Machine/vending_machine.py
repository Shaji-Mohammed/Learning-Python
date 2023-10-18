"""
Vending Machine Code here
"""
from InsufficientFunds import InsufficientFunds

valid_coin_values = [5, 10, 25, 100, 200]
reversed_list_coins = valid_coin_values
reversed_list_coins.reverse()
valid_products = {"drink": 2.75, "chips": 2.25, "candy": "3.15"}


def insert_coin(coin, inserted_coins):
    """
    This is called when a user inserts coins in the vending machine to purchase an item
    :param coin: Coin inserted by the user
    :param inserted_coins: List for keep track of the coins inserted
    :return:
    """
    if coin in valid_coin_values:
        inserted_coins.append(coin)
        return inserted_coins
    raise ValueError


def buy_product(product, balance):
    """
    :param product: Name of the product user wants to buy.
    :param balance: the amount the user currently has.
    :return: returns the balance after the product is purchased
    """
    if product not in valid_products.keys():
        raise ValueError
    if balance >= valid_products.get(product):
        return balance - valid_products.get(product)
    raise InsufficientFunds(f"Insufficient funds available to buy {product}")


def return_change(balance):
    """
    This method is called after the user purchases an item from the vending machine
    :param balance: The amount of money left after an item is purchased
    :return: returns the balance in change (coins)
    """
    change_left = []
    balance = balance * 100
    i = 0
    while balance > 0:
        while balance >= reversed_list_coins[i]:
            balance -= reversed_list_coins[i]
            change_left.append(reversed_list_coins[i])
        i += 1
    return change_left
