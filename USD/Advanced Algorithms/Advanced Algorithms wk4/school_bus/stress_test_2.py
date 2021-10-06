from itertools import permutations
import sys
import threading

sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size

INF = 10 ** 9


def optimal_path(graph):
    # This solution tries all the possible sequences of stops.
    # It is too slow to pass the problem.
    # Implement a more efficient algorithm here.
    n = len(graph)
    best_ans = INF
    best_path = []

    for p in permutations(range(n)):
        cur_sum = 0
        for i in range(1, n):
            if graph[p[i - 1]][p[i]] == INF:
                break
            cur_sum += graph[p[i - 1]][p[i]]
        else:
            if graph[p[-1]][p[0]] == INF:
                continue
            cur_sum += graph[p[-1]][p[0]]
            if cur_sum < best_ans:
                best_ans = cur_sum
                best_path = list(p)

    if best_ans == INF:
        return (-1, [])
    return (best_ans, [x + 1 for x in best_path])


def optimal_path_bf(graph, mask, pos, visited_all, dp, v, d):

    n = len(graph)
    if mask == visited_all:
        return graph[pos][0], v, d
    if dp[pos][mask]:
        # print("dynamic")
        return dp[pos][mask], v, d

    ans = INF
    for vertex in range(n):
        if mask & 1<<vertex == 0 and graph[pos][vertex] != INF:
            v.append(vertex + 1)
            x, y, z = optimal_path_bf(graph, mask | (1<<vertex), vertex, visited_all, dp, v, d)
            # Results from recursive call
            new_ans = graph[pos][vertex] + x
            if x >= INF:
                v.pop()
            ans = min(ans, new_ans)
            if pos == 0:
                # print("zero", v)
                set = []
                [set.append(x) for x in v if x not in set]
                if new_ans not in d:
                    d[new_ans] = set
                v = [1]
    dp[pos][mask] = ans
    return ans, v, d


def path(graph, ans):
    n = len(graph)
    for p in permutations(range(2, n+1)):
        # print(p)
        p = p[:0] + (1,) + p[0:]
        x = 0
        for i in range(len(p)):
            if x > ans:
                break
            if i < len(p) - 1:
                x += graph[p[i]-1][p[i+1]-1]
            else:
                x += graph[p[i]-1][p[0]-1]
                if x == ans:
                    return list(p)


def test():

    import random

    def length_by_path(g, p):
        out = 0
        for i in range(1, len(p)):
            out += g[p[i-1]-1][p[i]-1]

        out += g[p[-1]-1][0]
        return out

    weigths = list(range(1, 100)) + [INF]
    for n in range(5, 6):
        for _ in range(10):
            g = [[INF] * n for _ in range(n)]
            for u in range(n):
                for w in range(n):
                    if u != w:
                        wght = random.choice(weigths)
                        g[u][w] = wght
                        g[w][u] = wght

            visited_all = (1 << n) - 1
            dp = [[None for _ in range(2 ** (n))] for _ in range(n)]
            d = {}

            l, p = optimal_path(g)
            bl, bd, bpp = optimal_path_bf(g, 1, 0, visited_all, dp, [1], {})
            print(bl)
            mbp = min(bpp)
            bp = (bpp[mbp])
            print(bp)

            ll = length_by_path(g, bp)

            if l != bl or bl != ll:
                print('''
                NOT OK:
                graph: %s
                bf length: %s
                bf path: %s

                length: %s
                path: %s
                ll: %s
                        ''' % (g, bl, bp, l, p, ll))
                return
            else:
                print('%s: OK: %s' % (n, bl))

# print(test())
print(threading.Thread(target=test()).start())