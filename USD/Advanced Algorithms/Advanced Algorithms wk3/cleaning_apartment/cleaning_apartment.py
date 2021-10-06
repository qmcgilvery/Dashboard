# python3
import itertools
import os
# import pycosat

# f = open("test/01")
# n, m = map(int, f.readline().split())
# edges = [ list(map(int, f.readline().split())) for i in range(m) ]
n, m = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(m) ]
# print(edges)
perms = []
clauses = []
p = range(1, n+1)


def exactly_one_of(literals, z):
    z.append([l for l in literals])

    for pair in itertools.combinations(literals, 2):
        z.append([-l for l in pair])


def exactly_none_of(a, b, z):
    for i in range(len(a)):
        z.append([-a[i],-b[i]])
    # for pair in itertools.product(a, b):
    #     z.append([-l for l in pair])
        # z.append([l for l in pair])


def vertexPath():
    c = []
    z = []
    k = {}
    for x in range(1, n+1):
        k[x] = []
    for i in range(len(edges)):
        for j in range(1, len(edges[i])):
            k[edges[i][j-1]].append(edges[i][j])
            k[edges[i][j]].append(edges[i][j-1])
    # print(k)
    for i in range(1, n+1):
        c.append([])
        for j in range(1, n+1):
            c[i-1].append((i-1)*n+j)
    # print(c)
    for i in range(1, n):
        z.append([-i])
        for j in range(1, n):
            z[i-1].append(c[j][i])
    for i in range(1, n):
        if k[i+1]:
            for j in range(n-1):
                O = [c[x-1][j+1] for x in k[i+1]]
                O.insert(0, -c[i][j])
                z.append(O)
    for i in range(len(c)):
        exactly_one_of(c[i], z)
    for i in range(len(c)):
        s = i + 1
        f = k[s]
        for u in range(1, n+1):
            if u == s:
                pass
            elif u not in f:
                exactly_none_of(c[i], c[u-1], z)
    if len(edges)+1 < n:
        z.append([-1])
        z.append([1])
    # print(z)
    return z


def permutations(literals):

    for pair in itertools.permutations(literals, n-1):
        perms.append([l for l in pair])


def printEquisatisfiableSatFormula():

    # permutations(edges)
    # perms3 = validClauses(perms)
    # for i in range(len(perms3)):
    #     exactly_one_of(perms3[i])
    # for i in range(1, n+1):
    #     exactly_one_of([varnum(i, k) for k in color])
    c = vertexPath()
    # print(pycosat.solve(c))
    # with open('tmp.cnf', 'w') as f:
    #     f.write("p cnf {} {}\n".format(n*n, len(c)))
    #     for x in c:
    #         x.append(0);
    #         f.write(" ".join(map(str, x)) + "\n")
    #
    # os.system("cryptominisat5 tmp.cnf")
    for x in c:
        x.append(0);
    print(len(c), n*n)
    for y in c:
        print((" ".join(map(str, y))))

printEquisatisfiableSatFormula()
