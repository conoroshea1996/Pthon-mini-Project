from byotest import *


def get_change(amount):
    if amount == 0:
        return []
    if amount in [100, 50, 20, 10, 2, 1]:
        return [amount]

    change = []
    # change.append(2)
    # change.append(1)
    for coin in [100, 50, 20, 10, 2, 1]:
        if coin <= amount:
            amount -= coin
            change.append(coin)

    return change


test_are_equal(get_change(0), [])
test_are_equal(get_change(1), [1])
test_are_equal(get_change(2), [2])
test_are_equal(get_change(20), [20])
test_are_equal(get_change(50), [50])
test_are_equal(get_change(100), [100])
test_are_equal(get_change(3), [2, 1])
test_are_equal(get_change(3), [5, 2])
