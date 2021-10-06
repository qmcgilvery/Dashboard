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


def binary_correspondence(k):
    num = []
    z = list(bin(k+2)[2:])
    b = [int(y) for y in z]
    b.reverse()
    for i in range(len(z)):
        if z[i] == '1':
            num.append(i)
    # print (num)
    return num


def j_flip(k, j):
    x = k ^ (1<<j)
    print("J", x)
    return (x)


def optimal_path(graph):
    # This solution tries all the possible sequences of stops.
    # It is too slow to pass the problem.
    # Implement a more efficient algorithm here.
    n = len(graph)
    best_ans = INF
    best_path = []
    c = {}
    a = {}
    b = []
    for s in range(2,n):
        S = binary_correspondence(s)
        for _ in range(len(S)):
            # c{S}
            print(S)
        # for p in permutations(range(1, s+1)):
            # b.append(p)
            # p = p[:0] + (0,) + p[0:]
            # print(p)
        for i in S:
            if i != 0:
                for j in S:
                    remove_j = j_flip(S, j)
                    if j != i:
                        print(i, remove_j)
                        # c[S] = min(weight_sum_i(graph, p, i, n, c), weight_sum_j(graph, p, j, n, c) + graph[j][i])
            # if s == n - 1:
            #     a[p] = c[p]
    # print(c)
    # temp = list(a.values())
    # temp1 = min(a.values())
    # temp2 = list(a.keys())
    # temp3 = temp2[temp.index(temp1)]
    # best_ans = temp1
    # best_path = temp3

    if best_ans >= INF:
        return (-1, [])
    return (best_ans, [x + 1 for x in best_path])


t1 = time.time()

total = t1-t0
print(total)

# print_answer(*optimal_path(read_data()))
if __name__ == '__main__':
    print_answer(*optimal_path(read_data()))
