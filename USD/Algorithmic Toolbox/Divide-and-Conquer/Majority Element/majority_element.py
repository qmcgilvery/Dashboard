# python3


import random


def rand_num(x):
    randoms = []
    for i in range(x):
        randoms.append(random.randrange(1, 101, 1))
    return randoms


def majority_element_naive(elements):
    assert len(elements) <= 10 ** 5
    for e in elements:
        if elements.count(e) > len(elements) / 2:
            return 1
    return 0


def majority_element(elements):
    assert len(elements) <= 10 ** 5

    d = {}
    for e in elements:
        if e in d:
            d[e] += 1
        else:
            d[e] = 1
    for c in d:
        if d[c] > len(elements) / 2:
            return 1
    return 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element(input_elements))



