# from itertools import permutations
import itertools as it


def change(amount):
    assert (24 <= amount <= 1000)
    if amount == 24:
        return [5, 5, 7, 7]
    if amount == 25:
        return [5, 5, 5, 5, 5]
    if amount == 26:
        return [7, 7, 7, 5]
    if amount == 27:
        return [7, 5, 5, 5, 5]
    if amount == 28:
        return [7, 7, 7, 7]

    coins = change(amount - 5)
    coins.append(5)
    return coins


def sequence():
    return [(0, 1), (2, 3), (1, 2), (2, 3), (4, 5)]


def is_even(p):
    sign = 0
    for i in range(1, len(p)):
        for j in range(i - 1, -1, -1):
            # print(j, i)
            if p[j] > p[j + 1]:
                p[j], p[j + 1] = p[j + 1], p[j]
                sign = sign + 1
            else:
                break
    return sign % 2 == 0


# print(is_even([0, 3, 2, 4, 5, 6, 7, 1, 9, 8]))

# n = 10
# count = 0
#
# for i in range(n):
#     for j in range(n):
#         for k in range(n):
#             # print(i, j, k)
#             if i < j < k:
#                 count += 1


def count():
    counter = 0
    for d in it.product(range(9), repeat=4):
        if sum(d) == 9:
            counter += 1

    return counter


def count_wins(dice1, dice2):
    # assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins, dice2_wins = 0, 0

    for i in range(0, len(dice1)):
        for j in range(0, len(dice2)):
            if dice1[i] > dice2[j]:
                dice1_wins += 1
            if dice1[i] < dice2[j]:
                dice2_wins += 1

    return dice1_wins, dice2_wins


def find_the_best_dice(dices):
    assert all(len(dice) == 6 for dice in dices)
    ac = len(dices) - 1
    for i in range(0, len(dices)):
        value = []
        score = []
        for k in range(0, len(dices)):
            if k != i:
                total = count_wins(dices[i], dices[k])
                value.append(total)
        for j in range(0, len(value)):
            record = value[j][0] - value[j][1]
            if record > 0:
                score.append(record)
        if len(score) >= ac:
            return i
    else:
        return -1


def find_the_best(dices):
    assert all(len(dice) == 6 for dice in dices)
    a = len(dices)
    ac = len(dices) - 1
    value = []
    score = []
    for i in range(0, len(dices)):
        for k in range(0, len(dices)):
            # if k != i:
            total = count_wins(dices[i], dices[k])
            value.append(total)
    for j in range(0, len(value)):
        record = value[j][0] - value[j][1]
        score.append(record)
    scored = [score[o:o + a] for o in range(0, len(score), a)]
    return scored


def compute_strategy(dices):
    assert all(len(dice) == 6 for dice in dices)

    a = len(dices)
    strategy = dict()
    strategy["choose_first"] = True
    strategy["first_dice"] = 0
    choose_first = find_the_best(dices)
    all_positive = find_the_best(dices)
    remove_self = find_the_best(dices)
    for k in range(0, len(choose_first)):
        for n in choose_first[k]:
            if n <= 0:
                all_positive[k].remove(n)
    for j in range(0, len(all_positive)):
        if (len(all_positive[j]) + 1)/a == 1:
                strategy["choose_first"] = True
                strategy["first_dice"] = j
                return strategy
    for p in range(0, len(choose_first)):
        for i in range(0, len(choose_first)):
            if i == p:
                remove_self[p][i] = 1
        strategy[p] = remove_self[p].index(min(remove_self[p]))
        strategy["choose_first"] = False

    return strategy


print(compute_strategy([[1, 1, 4, 6, 7, 8], [2, 2, 2, 6, 7, 7], [3, 3, 3, 5, 5, 8]]))

# m = n
# seq = [m]
#
# while m > 1:
#     # if (m - 1) % 3 == 0:
#     #     m = m - 1
#     #     seq.append(m)
#     if m % 3 == 0:
#         m = m // 3
#         seq.append(m)
#     elif m % 2 == 0:
#         m = m // 2
#         seq.append(m)
#     else:
#         m = m - 1
#         seq.append(m)
#
# return len(seq), str(seq).strip('[]')
# print(count_wins([6, 6, 2, 2, 2, 5], [7, 4, 3, 2, 4, 2]))
