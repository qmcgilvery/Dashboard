# python3

EPS = 1e-6
PRECISION = 20


class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b


class Position:
    def __init__(self, column, row):
        self.column = column
        self.row = row


def ReadEquation():
    f = open("./tests/01")
    size = int(f.readline())
    # size = int(input())
    a = []
    b = []
    for row in range(size):
        line = list(map(float, f.readline().split()))
        # line = list(map(float, input().split()))
        a.append(line[:size])
        b.append(line[size])
    return Equation(a, b)


def SelectPivotElement(a, used_rows, used_columns):
    # This algorithm selects the first free element.
    # You'll need to improve it to pass the problem.
    pivot_element = Position(0, 0)
    while used_rows[pivot_element.row]:
        pivot_element.row += 1
    while used_columns[pivot_element.column] or a[pivot_element.row][pivot_element.column] == 0.0:
        pivot_element.column += 1
    return pivot_element


def SwapLines(a, b, used_rows, pivot_element):
    a[pivot_element.column], a[pivot_element.row] = a[pivot_element.row], a[pivot_element.column]
    b[pivot_element.column], b[pivot_element.row] = b[pivot_element.row], b[pivot_element.column]
    used_rows[pivot_element.column], used_rows[pivot_element.row] = used_rows[pivot_element.row], used_rows[pivot_element.column]
    pivot_element.row = pivot_element.column;


def ProcessPivotElement(a, b, pivot_element):
    # Write your code here
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
    # b[pivot_element.row] = b[pivot_element.row] - sum(a[pivot_element.row]) + 1


def MarkPivotElementUsed(pivot_element, used_rows, used_columns):
    used_rows[pivot_element.row] = True
    used_columns[pivot_element.column] = True


def SolveEquation(equation):
    a = equation.a
    b = equation.b
    size = len(a)

    used_columns = [False] * size
    used_rows = [False] * size
    for step in range(size):
        pivot_element = SelectPivotElement(a, used_rows, used_columns)
        SwapLines(a, b, used_rows, pivot_element)
        ProcessPivotElement(a, b, pivot_element)
        MarkPivotElementUsed(pivot_element, used_rows, used_columns)
    return b


def PrintColumn(column):
    size = len(column)
    for row in range(size):
        print("%.20lf" % column[row])


if __name__ == "__main__":
    equation = ReadEquation()
    solution = SolveEquation(equation)
    PrintColumn(solution)
    exit(0)
