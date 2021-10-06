# python3


def edit_distance(first_string, second_string):
    w, h = len(second_string) + 1, len(first_string) + 1
    D = [[float("inf") for x in range(w)] for y in range(h)]
    for a in range(len(first_string) + 1):
        D[a][0] = a
    for b in range(len(second_string) + 1):
        D[0][b] = b

    for i in range(1, len(first_string) + 1):
        for j in range(1, len(second_string) + 1):
            if first_string[i - 1] == second_string[j - 1]:
                diff = 0
            else:
                diff = 1
            D[i][j] = min(D[i-1][j] + 1, D[i][j-1] + 1, D[i-1][j-1] + diff)
    return D[len(first_string)][len(second_string)]


if __name__ == "__main__":
    print(edit_distance(input(), input()))

