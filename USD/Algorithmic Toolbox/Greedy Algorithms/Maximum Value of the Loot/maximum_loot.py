# python3

from __future__ import division
import math
from sys import stdin


# take the second element for sort
def take_first(elem):
    return elem[0]


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    order = [0] * len(prices)
    for i in range(len(prices)):
        order[i] = [prices[i] / weights[i], weights[i]]
    order = sorted(order, reverse=True, key=take_first)

    w = sorted(weights, reverse=True)
    p = sorted(prices, reverse=True)
    A = [0] * len(prices)
    v = 0
    for j in range(len(order)):
        if capacity == 0:
            return v
        a = min(order[j][1], capacity)
        v = v + a * order[j][0]
        order[j][1] = order[j][1] - a
        A[j] = A[j] + a
        capacity = capacity - a
    return round(v, 3)


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))

