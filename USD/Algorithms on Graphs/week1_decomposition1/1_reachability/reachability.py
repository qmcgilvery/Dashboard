#Uses python3

import sys


def reach(adj, x, y, v, visited_all):

    visited_all[x] = True
    for z in adj[x]:
        if not visited_all[z]:
            v.append(z)
            reach(adj, z, y, v, visited_all)
    if y in v:
        return 1
    else:
        return 0


if __name__ == '__main__':
    f = open("test.txt")
    input = f.read()
    # input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    visited = [[] for _ in range(n)]
    visited_all = [None for _ in range(n)]
    v = []
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
        visited[a - 1].append(None)
        visited[b - 1].append(None)
    print(reach(adj, x, y, v, visited_all))
