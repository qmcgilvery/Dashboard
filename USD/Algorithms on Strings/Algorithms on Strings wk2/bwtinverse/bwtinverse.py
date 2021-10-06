# python3
import sys

def rank(bwt):
    str = {}
    rank = []
    for s in bwt:
        if s not in str:
            str[s] = 0
        rank.append(str[s])
        str[s] += 1

    first_col = {}
    count = 0
    for c, s in sorted(str.items()):
        first_col[c] = count, count + s
        count += s


    reversed = 0
    text = []
    text.append('$')
    while bwt[reversed] != '$':
        c = bwt[reversed]
        text.append(c)
        reversed = first_col[c][0] + rank[reversed]

    text.reverse()
    return "".join(text).split()


def first(str):
    first_col = {}
    count = 0

    for c, s in sorted(str.items()):
        first_col[c] = count, count + s
        count += s
    return first_col


def test(bwt):
    a, b = rank(bwt)
    first_col = first(b)
    reversed = 0
    text = ['$']

    while bwt[reversed] != '$':
        c = bwt[reversed]
        text.append(c)
        reversed = first_col[c][0] + a[reversed]

    return reversed(text)


if __name__ == '__main__':
    # f = open("./sample_tests/sample2")
    # bwt = f.readline().strip()
    bwt = sys.stdin.readline().strip()
    print(*rank(bwt))