# python3
import itertools
from itertools import permutations
INF = 10 ** 9

import time

t0 = time.time()


def read_data():
    f = open("test/01")
    n, m = map(int, f.readline().split())
    graph = [[INF] * n for _ in range(n)]
    for _ in range(m):
        u, v, weight = map(int, f.readline().split())
        u -= 1
        v -= 1
        graph[u][v] = graph[v][u] = weight
    # n, m = map(int, input().split())
    # graph = [[INF] * n for _ in range(n)]
    # for _ in range(m):
    #     u, v, weight = map(int, input().split())
    #     u -= 1
    #     v -= 1
    #     graph[u][v] = graph[v][u] = weight
    return graph


def print_answer(path_weight, path):
    print(path_weight)
    if path_weight == -1:
        return
    print(' '.join(map(str, path)))


def weight_sum_i(graph, p, i, n, c):
    w = 0
    for j in range(len(p)-1):
        for i in range(1):
            for x in range(1):
                w += graph[p[i+j]][p[x+j+1]]
    if len(p) == n:
        w += graph[p[-1]][0]
    return w


def weight_sum_j(graph, p, j, n, c):
    w = 0
    z = p[:-1]
    for y in range(len(z)-1):
        for i in range(1):
            for x in range(1):
                w += graph[z[i+y]][z[x+y+1]]
    if len(p) == n:
        w += graph[p[-1]][0]
    return w

def permus(list):
    l = []
    # list = [x for x in list]
    if len(list) == 0:
        return []

    if len(list) == 1:
        return [list]

    for i in range(len(list)):
        m = list[i]
        newList = list[:i] + list[i+1:]

        for p in permus(newList):
            l.append([m] + p)
    return l



def optimal_path(graph):
    n = len(graph)
    A = [[{}]*(2**(n -1))] * (n-1)
    # A = {}
    # print(A)
    S = []
    print(graph)
    for s in range(2, n):
        S += permus(list(range(1, s+1)))
    for i in range(n):
        for j in range(2, n):
            A[i][j].update({(1, j): graph[1][j]})
    print(A)
    # for i in range(n-1):
    #     for j in range(2**(n -1)):
            # A[i][j].update({tuple(S[j]):graph[1][j]})
            # A[i][j].update({tuple(S[j]):i})
    # for x in range(2, n):


    # for i in range(len(A)):
    #     for s in range(1, n):
    #         S = permus(list(range(1, s + 1)))
    #         A[i] = S
    # for j in range(2, n):
    #     A[j] = {j:graph[1][j]}
    print(A)
    best_ans = INF
    best_path = []
    # for s in range(2,n-1):
    #     S = permus(list(range(1, s+1)))
    #     print(S)
    #     for k in S:
    #         print(k)
    #         o = tuple(k)
    #         A[o] = 1
    #         print(A)
    #         for m in S:
    #             p = tuple(m)
    #             A[o] = min(A[p])
    #             print(A)
    # print(A)

    if best_ans >= INF:
        return (-1, [])
    return (best_ans, [x + 1 for x in best_path])


t1 = time.time()

total = t1-t0
print(total)

# print_answer(*optimal_path(read_data()))
if __name__ == '__main__':
    print_answer(*optimal_path(read_data()))
