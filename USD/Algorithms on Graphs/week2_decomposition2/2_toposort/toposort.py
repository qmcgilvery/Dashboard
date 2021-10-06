# Uses python3

import sys
# from typing import List


class Vertex(object):

    def __init__(self):
        self.n = len(adj)
        self.color = ['white' for i in range(self.n)]
        # self.d = [0 for i in range(self.n)]
        # self.f = [0 for i in range(self.n)]
        # self.time = 0
        self.order = []

    def dfs(self, adj):
        post = 0
        for s in range(len(adj)):
            if self.color[s] == 'white':
                self.dfs_topsort(adj, s, post)
        return self.order

    def dfs_topsort(self, adj, x, post):
        self.color[x] = 'gray'
        # self.time += 1
        # self.d[x] = self.time
        for z in adj[x]:
            if self.color[z] == 'white':
                self.dfs_topsort(adj, z, post)
                post += 1
        self.color[x] = 'black'
        self.order.append(x)
        # self.time += 1
        # self.f[x] = self.time
        return self.order


if __name__ == '__main__':
    # f = open("../1_acyclicity/test.txt")
    # input = f.read()
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    visited = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    a = Vertex()
    order = a.dfs(adj)
    order.reverse()
    # new_order = []
    # m = max(order)
    # for x in range(len(order) - 1):
    #     ind = order.index(m)
    #     new_order.append(ind)
    #     m = max(i for i in order if i < m)
    # new_order.append(order.index(min(order)))
    # print(new_order)
    # order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')
