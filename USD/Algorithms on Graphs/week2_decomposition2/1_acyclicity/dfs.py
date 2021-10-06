#Uses python3

import sys

# parent = {}


def dfs(adj, parent):

    for s in range(len(adj)):
        if s not in parent:
            parent[s] = None
            dfs_visit(adj, s, parent)
    for x in range(len(parent)):
        if 'r' in parent[x]:
            return 1
        else:
            return parent


def dfs_visit(adj, x, parent):

    for z in adj[x]:
        if z not in parent:
            parent[z] = x
            dfs_visit(adj, z, parent)
        else:
            parent[z] = 'r'
    return parent


if __name__ == '__main__':
    f = open("test.txt")
    input = f.read()
    # input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    # visited = [None for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    visited = [[] for _ in range(n)]
    # for i in range(len(adj)):
    #     visited.append([i])
    print(dfs(adj, {}))



# def dfs(adj, used, order, x):
#     #write your code here
#     pass


# def toposort(adj):
#     used = [0] * len(adj)
#     order = []
#     dfs(adj, order)
#     #write your code here
#     return order