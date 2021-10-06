# python3
import sys
from itertools import product


def partition2(arr, divisor, n, summ):
    p = []
    b = []
    # Instantiate dp table
    d = [[False] * (len(arr) + 1) for _ in range(sum(arr) // divisor + 1)]
    d[0][0] = True
    av = sum(arr) // divisor
    # Populate dp table
    for i in range(1, len(arr) + 1):
        for w in range(av + 1):
            if arr[i - 1] > w:
                d[w][i] = d[w][i - 1]
            else:
                d[w][i] = d[w][i - 1] or d[w - arr[i - 1]][i - 1]
    arr = list(arr)
    arr.insert(0, 0)
    # Fill bin 1 with list elements that sum to average
    return printSubsetsRec(arr, n - 1, summ, p, d, b)


def printSubsetsRec(arr, i, summ, p, d, b):
    if summ == 0:
        return p
    if i == 0:
        return 0
    if d[summ][i-1]:
        b = []
        b.extend(p)
        return printSubsetsRec(arr, i - 1, summ, b, d, b)
    if sum >= arr[i] and d[summ-arr[i]][i-1]:
        p.append(arr[i])
        return printSubsetsRec(arr, i - 1, summ - arr[i], p, d, b)
    else:
        return printSubsetsRec(arr, i - 1, summ, p, d, b)


def partition3(souvenirs):
    assert 1 <= len(souvenirs) <= 20
    assert all(1 <= v <= 30 for v in souvenirs)
    av = sum(souvenirs) // 3
    tmp = list(souvenirs)
    n = len(souvenirs)
    if sum(souvenirs) % 3 != 0:
        return 0

    # Build dp table and get bin 1
    d = partition2(souvenirs, 3, n, av)
    # Remove bin 1 values from souvenirs
    for value in sorted(d, reverse=True):
        tmp.remove(value)
    n2 = len(tmp)
    r = partition2(tmp, 2, n2, av)
    if sum(d) == sum(r):
        return 1
    else:
        return 0

# if __name__ == '__main__':
#     input_n, *input_values = list(map(int, stdin.read().split()))
#     assert input_n == len(input_values)
#     print(partition3(input_values))


# if __name__ == '__main__':
#     input = sys.stdin.read()
#     n, *souvenirs = list(map(int, input.split()))
#     print(partition3(souvenirs))

# print(partition3((1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19, 25)))
# print(partition3((1, 2, 3, 4, 5, 5, 7, 7, 8, 10, 12, 19)))
