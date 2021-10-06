# python3
import sys


def convert_characters(string):

    if string == '$':
        return 0
    if string == 'A':
        return 1
    if string == 'C':
        return 2
    if string == 'G':
        return 3
    if string == 'T':
        return 4


def sort_characters(S):
    order = [None] * len(S)
    count = [0] * 5

    for i in S:
        x = convert_characters(i)
        count[x] = count[x] + 1
    for j in range(1, len(count)):
        count[j] = count[j] + count[j - 1]
    for i in range(len(S) - 1, -1, -1):
        c = convert_characters(S[i])
        count[c] = count[c] - 1
        order[count[c]] = i

    return order


def sort_doubles(S, L, order, classe):
    new_order = [None] * len(S)
    count = [0] * len(S)

    for i in range(len(S)):
        count[classe[i]] = count[classe[i]] + 1
    for j in range(1, len(S)):
        count[j] = count[j] + count[j - 1]
    for i in range(len(S) - 1, -1, -1):
        start = (order[i] - L + len(S)) % len(S)
        cl = classe[start]
        count[cl] = count[cl] - 1
        new_order[count[cl]] = start

    return new_order

# [2, 3, 7, 12, 4, 10, 6, 13, 8, 15, 14, 9, 5, 11, 1, 0]

def compute_class(S, order):

    classe = [None] * len(S)
    classe[order[0]] = 0

    for i in range(1, len(S)):
        if S[order[i]] != S[order[i - 1]]:
            classe[order[i]] = classe[order[i - 1]] + 1
        else:
            classe[order[i]] = classe[order[i - 1]]
    return classe


def update_class(new_order, classe, L):
    n = len(new_order)
    new_classe = [None] * n
    new_classe[new_order[0]] = 0

    for i in range(1, n):
        cur = new_order[i]
        pre = new_order[i-1]
        mid = (cur + L) % n
        midprev = (pre + L) % n
        if classe[cur] != classe[pre] or classe[mid] != classe[midprev]:
            new_classe[cur] = new_classe[pre] + 1
        else:
            new_classe[cur] = new_classe[pre]
    return new_classe


def build_suffix_array(S):
    order = sort_characters(S)
    classe = compute_class(S, order)
    L = 1
    while L <= len(S):
        order = sort_doubles(S, L, order, classe)
        classe = update_class(order, classe, L)
        L *= 2

    return order


# f = open("./sample_tests/sample2")
# text = f.readline().strip()
# # print(sort_characters(text))
# print(build_suffix_array(text))
# print(len(text))

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(" ".join(map(str, build_suffix_array(text))))
