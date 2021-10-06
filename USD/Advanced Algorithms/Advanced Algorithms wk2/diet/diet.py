# python3
from sys import stdin
import itertools
import copy



# python3

EPS = 1e-5
PRECISION = 20

class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Position:
    def __init__(self, column, row):
        self.column = column
        self.row = row


def SelectPivotElement(a, used_rows, used_columns):
    pivot_element = Position(0, 0)
    while used_rows[pivot_element.row]:
        pivot_element.row += 1
    while used_columns[pivot_element.column] or a[pivot_element.row][pivot_element.column] == 0.0:
        pivot_element.column += 1
        if pivot_element.column >= len(a[pivot_element.row]):
            return False
    return pivot_element


def SwapLines(a, b, used_rows, pivot_element):
    a[pivot_element.column], a[pivot_element.row] = a[pivot_element.row], a[pivot_element.column]
    b[pivot_element.column], b[pivot_element.row] = b[pivot_element.row], b[pivot_element.column]
    used_rows[pivot_element.column], used_rows[pivot_element.row] = used_rows[pivot_element.row], used_rows[pivot_element.column]
    pivot_element.row = pivot_element.column;


def ProcessPivotElement(a, b, pivot_element):
    size = len(a)
    var = a[pivot_element.row][pivot_element.column]
    a[pivot_element.row] = [x / var for x in a[pivot_element.row]]
    b[pivot_element.row] = b[pivot_element.row] / var
    for i in range(size):
        if i != pivot_element.row:
            new = a[i][pivot_element.column]
            temp_a = [x * new for x in a[pivot_element.row]]
            temp_b = b[pivot_element.row] * new
            a[i] = [a_i - b_i for a_i, b_i in zip(a[i], temp_a)]
            b[i] = b[i] - temp_b

def MarkPivotElementUsed(pivot_element, used_rows, used_columns):
    used_rows[pivot_element.row] = True
    used_columns[pivot_element.column] = True


def SolveEquation(ap, bp):
    a = copy.deepcopy(ap)
    b = copy.deepcopy(bp)
    size = len(a)
    wide = len(a[0])

    used_columns = [False] * wide
    used_rows = [False] * size
    for step in range(size):
        pivot_element = SelectPivotElement(a, used_rows, used_columns)
        if not pivot_element:
            break
        SwapLines(a, b, used_rows, pivot_element)
        ProcessPivotElement(a, b, pivot_element)
        MarkPivotElementUsed(pivot_element, used_rows, used_columns)
    return b


def PrintColumn(column):
    size = len(column)
    for row in range(size):
        print("%.20lf" % column[row])


def find_subsets(a, b, n):
  return [list(x) for x in itertools.combinations(a, n)]


def find_max_value(A, c):
    value_list = [c_i / a_i for c_i, a_i in zip(c, A[0])]
    max_index = value_list.index(max(value_list))
    return max_index


def check_for_negatives(A):
    for i in range(len(A)-(m+1)):
        if min(A[i]) < 0:
            return True
    return False


def check_validity(row, B):
    for i in range(len(row)):
        if sum(row[i]) > B[i]+EPS:
            return False
    return True


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


def solve_diet_problem(n, m, A, b, c):
    ans_t = 0

    ans_x = [0.00000000000000] * m
    a_t = [-99999999999999]
    for i in range(len(A)):
        A[i].append(B[i])
    if n == 1:
        combo = [A[0]]
    else:
        combo = find_subsets(A, b, m)
    if n > 1:
        combo, new_b = mutate_combo(combo)
    else:
        combo, new_b = mutate_combo_n1(combo)

    ans = [-99999999999]
    for i in range(len(combo)):
        size = len(combo[i])
        length = size * i
        a = combo[i]
        q = combo.index(combo[i]) * 2
        b = new_b[length:length + size]
        # if n == 1 and 0 not in A[0] and A[0][0] * c[0] > 0 and not check_for_negatives(A):
        #     ans_1 = [x / y for x, y in zip(c, combo[0][:m])]
        #     ans_2 = ans_1.index(max(ans_1))
        #     ans_3 = B[0] / A[0][ans_2]
        #     ans_4 = [0.00000000000000] * m
        #     ans_4[ans_2] = ans_3
        #     ans_x = ans_4
        #     return ans_t, ans_x
        if n > 1:
            # z = [-0.000000000000000000, 26.675675675675677000, -0.000000000000000000, -0.000000000000000000]
            z = SolveEquation(a, b)
        elif max(c) <= 0:
            ans_x = [0.00000000000000] * m
            return ans_t, ans_x
        elif min(a) <= 0 < max([1 if y_i > 0 and x_i <= 0 else x_i * y_i for x_i, y_i in zip(A[0], c)]):
            ans_t = 1
            return ans_t, ans_x
        elif 0 < max([1 if y_i > 0 and x_i <= 0 else x_i * y_i for x_i, y_i in zip(A[0], c)]):
            max_index = find_max_value(A, c)
            z = b[0]/a[max_index]
            ans_x[max_index] = z
            return ans_t, ans_x
        else:
            max_index = find_max_value(A, c)
            z = [b[0] / a[max_index]]
        row = [[0] * m] * (m+n)
        for u in range(n+m):
            row[u] = [(a_i * z_i) for a_i, z_i in zip(A[u], z)]
        if check_validity(row, B):
            t = [0] * n
            for x in range(n):
                k = 0
                for g in range(m):
                    t[x] += z[k] * c[k]
                    k += 1
            # for e in range(n):
            #     if t[e] > a_t[e]:
            #         a_t[e] = t[e]
            #         ans = z
            if t[0] > a_t[0]:
                a_t = [t[0]]
                ans = z
    # an_i = a_t.index(max(a_t))
    # an = ans[an_i]
    if -99999999999 in ans:
        ans_t = -1
    else:
        ans_x = ans
    if sum(ans_x) >= 999999999.9999999:
        ans_t = 1
        return ans_t, ans_x
    # print(a_t)
    return ans_t, ans_x

n, m = list(map(int, stdin.readline().split()))
A = []
for i in range(n):
  A += [list(map(int, stdin.readline().split()))]
B = list(map(int, stdin.readline().split()))
c = list(map(int, stdin.readline().split()))
# f = open("tests/81")
# n, m = list(map(int, f.readline().split()))
# A = []
# for i in range(n):
#     A += [list(map(int, f.readline().split()))]
for i in range(m):
    x = [0] * m
    x[i] = -1
    A.append(x)
inf = [1 for x in A[0]]
A.append(inf)
# B = list(map(int, f.readline().split()))
for i in range(m):
    B.append(0)
B.append(10**9+EPS)
# c = list(map(int, f.readline().split()))

anst, ansx = solve_diet_problem(n, m, A, B, c)

if anst == -1:
  print("No solution")
if anst == 0:  
  print("Bounded solution")
  print(' '.join(list(map(lambda x : '%.18f' % x, ansx))))
if anst == 1:
  print("Infinity")
    
