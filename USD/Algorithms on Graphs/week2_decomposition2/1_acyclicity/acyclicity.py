#Uses python3

import sys


# def acyclic(adj, parent):
#
#     for s in range(len(adj)):
#         if s not in parent:
#             b = s
#             parent[s] = None
#             dfs_visit(adj, s, parent, b)
#     for x in range(len(parent)):
#         if parent[x] == 'r':
#             return 1
#
#     return 0
#
#
# def dfs_visit(adj, x, parent, b):
#
#     for z in adj[x]:
#         if z not in parent:
#             parent[z] = x
#             dfs_visit(adj, z, parent, b)
#         elif z == b:
#             parent[z] = 'r'
#     return parent

def acyclic(adj, x, visited, pre, post):

    global posts
    posts = post
    # visited[x].append(pre)
    for z in adj[x]:
        pre += 1
        acyclic(adj, z, visited, pre, posts)
        posts += 1
    visited[x].append(posts)

    return sorted(visited)


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
    print(acyclic(adj, 0, visited, 0, 0))
