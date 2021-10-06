# python3
from sys import stdin
import numpy as np
import itertools
import copy

EPS = 1e-6


def find_subsets(a, b, n):
    return [list(x) for x in itertools.combinations(a, n)]
    # x = map(list, itertools.combinations(a, n))
    # return x


def check_for_negatives(A):
    for i in range(len(A)):
        if min(A[i]) < 0:
            return True
    return False


def check_for_zeroes(A, c):
    for i in range(len(A)):
        inf = [x * y if x > 0 and y != 0 else "Infinity" for x, y in zip(A[i], c)]
        if "Infinity" in inf:
            return True
    return False


def check_validity(row, B):
    for i in range(len(row)):
        if sum(row[i]) > B[i]:
            return False
    return True


def mutate_combo(combo):
    mutated = []
    new_b = []
    for x in range(len(combo)):
        for j in combo[x]:
            new_b.append(j[-1])
            if j not in mutated:
                mutated.append(j)
    mutate = []
    for x in range(len(combo)):
        for j in combo[x]:
            if j not in mutate:
                j.pop()
                mutate.append(j)
    return combo, new_b


def mutate_combo_n1(combo):
    mutated = []
    new_b = []
    for j in combo:
        new_b.append(j[-1])
        if j not in mutated:
            mutated.append(j)
    mutate = []
    for j in combo:
        if j not in mutate:
            j.pop()
            mutate.append(j)
    return combo, new_b


def solve_diet_problem(n, m, A, B, c):
    # Write your code here
    anst = 0
    ans = [-99999999999] * n
    ans_y = []
    ans_x = [0] * n
    t = [0] * n
    for i in range(len(A)):
        A[i].append(B[i])
    if n == 1:
        combo = [A[0]]
    else:
        combo = find_subsets(A, B, m)
    if len(combo) == 0:
        anst = 1
        return anst, ans_x
    if n == 1 and 0 not in A[0] and A[0][0] * c[0] > 0 and not check_for_negatives(A):
        ans_1 = [x / y for x, y in zip(c, combo[0][:m])]
        ans_2 = ans_1.index(max(ans_1))
        ans_3 = B[0] / A[0][ans_2]
        ans_4 = [0.00000000000000] * m
        ans_4[ans_2] = ans_3
        ans_x = ans_4
        return anst, ans_x
    if m == 1 and c[0] <= 0:
        ans_x = [0.00000000000000]
        return anst, ans_x
    else:
        if n > 1:
            combo, new_b = mutate_combo(combo)
        else:
            combo, new_b = mutate_combo_n1(combo)
        for i in range(len(combo)):
            size = len(combo[i])
            length = size * i
            a = np.array(combo[i])
            q = combo.index(combo[i]) * 2
            b = np.array(new_b[length:length+size])
            # if max(t) <= 0:
            #     return anst, ans_x
            try:
                z = np.linalg.solve(a, b)
            except:
                anst = -1
                # return anst, ans_x
            if len(z) == 1 and z[0] <= 0:
                anst = 1
                return anst, ans_x
            row = [[0] * m] * n
            for u in range(n):
                row[u] = [a_i * z_i for a_i, z_i in zip(A[u], z)]
            if check_validity(row, B):
                for x in range(len(row)):
                    t[x] = sum([x_i * c_i for x_i, c_i in zip(row[x], c)])
                ind = t.index(max(t))
                if max(t) <= 0:
                    return anst, ans_x
                ans[i] = [x_i * y_i for x_i, y_i in zip(A[ind], z)]
        # for i in range(len(ans)):
        #     if ans[i] != -99999999999:
        #         ans_y.append(sum([a_i for a_i in ans[i]]))
        #     else:
        #         ans_y.append(-99999999999)
        an_i = t.index(max(t))
        an = ans[an_i]
        # ans_x = [0] * n
        if an == -99999999999:
            anst = -1
        else:
            ans_x = [a_i / z_i if a_i != 0.0 else 0 for a_i, z_i in zip(an, A[an_i])]
        return anst, ans_x


    # return [0, [0] * m]


# n, m = list(map(int, stdin.readline().split()))
# A = []
# for i in range(n):
#   A += [list(map(int, stdin.readline().split()))]
# B = list(map(int, stdin.readline().split()))
# c = list(map(int, stdin.readline().split()))
f = open("tests/11")
n, m = list(map(int, f.readline().split()))
A = []
for i in range(n):
    A += [list(map(int, f.readline().split()))]
# for i in range(m):
#     x = [0] * m
#     x[i] = -1
#     A.append(x)
B = list(map(int, f.readline().split()))
# for i in range(m):
#     B.append(0)
c = list(map(int, f.readline().split()))

anst, ansx = solve_diet_problem(n, m, A, B, c)

if anst == -1:
    print("No solution")
if anst == 0:
    print("Bounded solution")
    print(' '.join(list(map(lambda x: '%.18f' % x, ansx))))
if anst == 1:
    print("Infinity")
