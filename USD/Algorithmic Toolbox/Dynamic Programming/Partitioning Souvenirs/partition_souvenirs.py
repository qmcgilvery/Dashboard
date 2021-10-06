# python3
import sys
from itertools import product

v = []

def partition2(arr, divisor, n, summ):
    p = []
    b = []
    # Instantiate dp table
    d = [[False] * (len(arr)) for _ in range(sum(arr) // divisor + 1)]
    d[0][0] = True
    av = sum(arr) // divisor
    # Populate dp table
    for i in range(1, len(arr)):
        for w in range(av + 1):
            if arr[i - 1] > w:
                d[w][i] = d[w][i - 1]
            else:
                d[w][i] = d[w][i - 1] or d[w - arr[i - 1]][i - 1]
    arr = list(arr)
    arr.insert(0, 0)
    # Fill bin 1 with list elements that sum to average
    return printSubsetsRec(arr, n, summ, p, d)


def printSubsetsRec(arr, i, summ, p, d):
    if i == 0 & summ != 0 & d[summ][0]:
        p.append(arr[i])
        v.append(p)
        # p[:] = []
        return
    if i == 0 & summ == 0:
        v.append(p)
        # p[:] = []
        return
    if d[summ][i - 1]:
        b = []
        b.extend(p)
        printSubsetsRec(arr, i - 1, summ, b, d)
    if summ >= arr[i] and d[summ - arr[i]][i - 1]:
        p.append(arr[i])
        printSubsetsRec(arr, i - 1, summ - arr[i], p, d)
    # else:
    #     b = []
    #     b.extend(p)
    #     printSubsetsRec(arr, i - 1, summ, b, d)
    return v

def partition3(souvenirs):
    assert 1 <= len(souvenirs) <= 20
    assert all(1 <= v <= 30 for v in souvenirs)
    if sum(souvenirs) % 3 != 0 or len(souvenirs) < 3:
        return 0
    av = sum(souvenirs) // 3
    n = len(souvenirs)
    # tmp = list(souvenirs)
    # Build dp table and get bin 1
    d = partition2(souvenirs, 3, n, av)
    if d == 0:
        return 0
    # Remove bin 1 values from souvenirs
    global v
    v = []
    for elem in range(len(d)):
        tmp = list(souvenirs)
        for value in sorted(d[elem], reverse=True):
            tmp.remove(value)
        n2 = len(tmp)
        r = partition2(tmp, 2, n2, av)
        if r:
            return 1
    return 0


# # if __name__ == '__main__':
# #     input_n, *input_values = list(map(int, stdin.read().split()))
# #     assert input_n == len(input_values)
# #     print(partition3(input_values))
#
#
# if __name__ == '__main__':
#     input = sys.stdin.read()
#     n, *souvenirs = list(map(int, input.split()))
#     print(partition3(souvenirs))


# print (partition3((3, 3, 3)))

