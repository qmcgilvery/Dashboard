# python3
import itertools
import os

f = open("test/01")
n, m = map(int, f.readline().split())
edges = [list(map(int, f.readline().split())) for i in range(m)]
# n, m = map(int, input().split())
# edges = [ list(map(int, input().split())) for i in range(m) ]
clauses = []
color = range(1, 4)


def varnum(node, k):
    return node + k


def varnum_edge(i, k):
    return (i-1)*3 + k


def exactly_one_color_of(a, b):
    c = [0] * len(a)
    for i in range(len(a)):
        c[i] = [-a[i], -b[i]]
    for i in range(len(c)):
        clauses.append(c[i])


def exactly_one_of(literals):
    clauses.append([l for l in literals])

    for pair in itertools.combinations(literals, 2):
        clauses.append([-l for l in pair])


def printEquisatisfiableSatFormula():
    # each vertex contains exactly one color
    node = 0
    for i in range(1, n+1):
        exactly_one_of([varnum(node, k) for k in color])
        node = 3 + node

    # k appears exactly once in adjacent vertices
    for (i, j) in edges:
        a = [varnum_edge(i, k) for k in color]
        b = [varnum_edge(j, k) for k in color]
        exactly_one_color_of(a, b)


    with open('tmp.cnf', 'w') as f:
        f.write("p cnf {} {}\n".format(n, len(clauses)))
        for c in clauses:
            c.append(0);
            f.write(" ".join(map(str, c)) + "\n")
    # for c in clauses:
    #     c.append(0)
    # print(len(clauses), n*3)
    # for x in clauses:
    #     print((" ".join(map(str, x))))
    os.system("cryptominisat5 tmp.cnf")

printEquisatisfiableSatFormula()