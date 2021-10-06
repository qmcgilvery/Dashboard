# python3
import time
import random
from operator import itemgetter
from itertools import permutations, combinations

INF = 10 ** 9

f = open("test/05")
n, m = map(int, f.readline().split())
graph = [[INF] * n for _ in range(n)]
for _ in range(m):
    u, v, weight = map(int, f.readline().split())
    u -= 1
    v -= 1
    graph[u][v] = graph[v][u] = weight
visited_all = (1 << n) - 1
v = []
v.append(1)
dp = [[None for _ in range(2 ** (n))] for _ in range(n)]
f.close()


def read_data():
    f = open("test/05")
    n, m = map(int, f.readline().split())
    graph = [[INF] * n for _ in range(n)]
    for _ in range(m):
        u, v, weight = map(int, f.readline().split())
        u -= 1
        v -= 1
        graph[u][v] = graph[v][u] = weight
    f.close()
    return graph


def create_graph(n, dist3):
    graph = [[INF] * n for _ in range(n)]
    for d3 in dist3:
        u = d3[0] - 1
        v = d3[1] - 1
        weight = d3[2]
        graph[u][v] = graph[v][u] = weight
    return graph


def print_answer(path_weight, path, all_paths=False):
    print(path_weight)
    if path_weight == -1:
        return

    if not all_paths:
        print(' '.join(map(str, path)))
    else:
        for p in path:
            print(' '.join(map(str, p)))


def optimal_path(graph, all_paths=False):
    # This solution tries all the possible sequences of stops.
    # It is too slow to pass the problem.
    # Implement a more efficient algorithm here.
    n = len(graph)
    best_ans = INF
    best_path = []

    for p in permutations(range(n)):
        if p[0] != 0:
            break
        cur_sum = 0
        for i1 in range(1, n):
            if graph[p[i1 - 1]][p[i1]] == INF:
                break
            cur_sum += graph[p[i1 - 1]][p[i1]]
        else:
            if graph[p[-1]][p[0]] == INF:
                continue
            cur_sum += graph[p[-1]][p[0]]
            if cur_sum <= best_ans:
                best_ans = cur_sum
                if not all_paths:
                    best_path = list(p)
                else:
                    if cur_sum < best_ans:
                        best_path = list()
                    best_path.append(list(p))

    if best_ans == INF:
        return -1, []

    for b in best_path:
        for i1 in range(0, len(b)):
            b[i1] += 1

    return best_ans, best_path


if __name__ == '__main__':

    compare = True
    try_number = 1
    success = 1000  # tries to success
    max_dist = 10 ** 1
    max_nodes = 5

    print('\n')
    print('======= OUTPUT =======')
    print('=== SLOW ====')
    start = time.time()
    best, best_list = optimal_path(read_data(), True)
    end = time.time()
    print('=== SLOW time: {} seconds ==='.format(end - start))
    print('= Results: =')
    print_answer(best, best_list, True)

    print('=== DYNAMIC ====')
    start = time.time()
    clock = 1


    # HERE YOU SHOULD IMPLEMENT YOUR TSP FUNCTION
    # visited_all = (1 << n) - 1
    # v = [None] * n
    # v[0] = 1
    # dp = [[None for _ in range(2 ** (n))] for _ in range(n)]

    def tsp(mask, pos):

        if mask == visited_all:
            return graph[pos][0], v
        if dp[pos][mask]:
            return dp[pos][mask], v

        ans = INF

        for vertex in range(n):
            if mask & 1 << vertex == 0 and graph[pos][vertex] != INF:
                x, y = tsp(mask | (1 << vertex), vertex)
                new_ans = graph[pos][vertex] + x
                if vertex + 1 not in v and x != INF:
                    v.append(vertex + 1)
                ans = min(ans, new_ans)
        dp[pos][mask] = ans
        return ans, v


    best_d, best_list_d = tsp(1, 0)
    end = time.time()
    print('=== DYNAMIC time: {} seconds ==='.format(end - start))
    print('= Results: =')
    print_answer(best_d, best_list_d)

    if best == best_d:
        if best != -1:
            compare = False
            for b_list in best_list:
                if b_list == best_list_d:
                    compare = True
                    break
    else:
        compare = False

    if not compare:
        print('===== NO COMPARE ======')

    try_number += 1

    if try_number == success + 1:
        print('\n')
        print('=====SUCCESS AFTER {} TRIES =================='.format(try_number - 1))
