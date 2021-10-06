import random

row = [i for i in range(4)]


def make_vector(new_row):
    puzzle = [[None] * 4 for _ in range(4)]
    for i in range(len(new_row)):
        for j in range(4):
            puzzle[i][j] = j + 1
    return puzzle


def permute_vector(new_row, p):
    for x in range(p):
        store = new_row.pop(len(new_row) - 1)
        new_row.insert(0, store)
    return new_row


def permute_row(puzzle, x, y, z):
    permute_vector(puzzle[1], x)
    permute_vector(puzzle[2], y)
    permute_vector(puzzle[3], z)
    return puzzle


def linear_search(vector, item):
    for i in range(1, len(vector)):
        if item in vector:
            return True
    return False


def check_column(puzzle, j):
    temp = []
    for k in range(len(puzzle)):
        temp.append(puzzle[k][j])
    for k in range(1, 5):
        if not linear_search(temp, k):
            return False
    return temp


def col_check(puzzle):
    for x in range(len(puzzle)):
        if not check_column(puzzle, x):
            return False
    return True


def check_grid(puzzle, row1, col1, row2, col2):
    temp = [puzzle[row1][col1], puzzle[row1][col2], puzzle[row2][col1], puzzle[row2][col2]]
    for k in range(1, 5):
        if not linear_search(temp, k):
            return False
    return temp


def check_grids(puzzle):
    for k in range(2):
        for j in range(2):
            if not check_grid(puzzle, 2 * k, 2 * j, 1 + 2 * k, 1 + 2 * j):
                return False
    return True


def make_solution(row):
    puzzle = make_vector(row)

    while not (col_check(puzzle) and check_grids(puzzle)):
        x = random.randint(0, 3)
        y = random.randint(0, 3)
        z = random.randint(0, 3)

        permute_row(puzzle, x, y, z)

    return puzzle

def make_puzzle(puzzle, n):
    while n > 0:
        for i in range(len(puzzle)):
            x = random.randint(0, 3)
            if puzzle[i][x] and n > 0:
                print(puzzle[i][x])
                puzzle[i][x] = None
                n -= 1
                print(n)
    return puzzle


print(make_puzzle(make_solution(row), 0))

