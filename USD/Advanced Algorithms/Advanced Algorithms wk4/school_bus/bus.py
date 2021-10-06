# python3
import itertools
from itertools import permutations
import sys
import threading

sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size

INF = 10 ** 9 + 10

# f = open("test/01")
# n, m = map(int, f.readline().split())
# graph = [[INF] * n for _ in range(n)]
# for _ in range(m):
#     u, v, weight = map(int, f.readline().split())
#     u -= 1
#     v -= 1
#     graph[u][v] = graph[v][u] = weight

# graph = [[1000000000, 35, 13, 19, 48], [35, 1000000000, 75, 76, 73], [13, 75, 1000000000, 51, 87], [19, 76, 51, 1000000000, 71], [48, 73, 87, 71, 1000000000]]
# n = len(graph)
# m = len(graph[0])

n, m = map(int, input().split())
graph = [[INF] * n for _ in range(n)]
for _ in range(m):
    u, v, weight = map(int, input().split())
    u -= 1
    v -= 1
    graph[u][v] = graph[v][u] = weight

visited_all = (1<<n)-1
dp = [[None for _ in range(2 ** n)] for _ in range(n)]

def optimal_path(mask, pos, v, d, k, r, c):

    if mask == visited_all:
        # print("base_case", v)
        c = 0
        y = tuple(v)
        return graph[pos][0], y, d, k, r, c
    # if dp[pos][mask]:
    #     return dp[pos][mask], y, d, k, r, c
    ans = INF
    y = tuple(v)
    for vertex in range(n):
        if mask & 1<<vertex == 0:
            v.append(vertex + 1)
            x, y, z, k, r, c = optimal_path(mask | (1<<vertex), vertex, v, d, k, r, c)
            new_ans = graph[pos][vertex] + x
            ans = min(ans, new_ans)
            c += 1
            nu = y[-(c+1):]
            if c < n-1:
                k[nu] = new_ans
            v.pop()

    # dp[pos][mask] = ans
    return ans, y, d, k, r, c


def main():

    x, y, z, k, b, r = optimal_path(1, 0, [1], {}, {}, 2, 0)
    # print(k)
    g = {h:v+graph[0][h[0]-1] for (h,v) in k.items() if len(h) == n-1}
    # print(g)
    q = list(min(g))
    j = list(q)
    j.insert(0, 1)


    if x >= INF:
        print(-1)
    else:
        print(x)
        print(*j)

# 243
# [1, 2, 3, 4, 5] b
# [1, 2, 3, 5, 4] g


# main()
# path(graph, 97)
threading.Thread(target=main()).start()
# if __name__ == '__main__':
#     print_answer(*optimal_path(1, 0))
