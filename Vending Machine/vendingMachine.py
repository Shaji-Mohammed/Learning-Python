"""
Vending Machine Code here
"""

valid_coin_values = [5, 10, 25, 100, 200]
valid_products = {"drink" : 2.75, "chips" : 2.25, "candy" : "3.15"}


def insert_coin(coin, inserted_coins):
    if coin in valid_coin_values:
        inserted_coins.append(coin)
        return inserted_coins
    raise ValueError


def buy_product(product, balance):
    if product in valid_products.keys():
        return balance - valid_products.get(product)
    raise ValueError
