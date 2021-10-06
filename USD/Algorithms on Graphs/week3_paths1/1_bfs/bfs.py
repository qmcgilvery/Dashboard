#Uses python3

import sys
import queue


class Bfs(object):

    def __init__(self):
        self.n = len(adj)
        self.col = ['white' for i in range(self.n)]
        self.dis = [n + 1 for i in range(self.n)]
        self.par = [None for i in range(self.n)]
        # self.q = queue.Queue

    def distance(self, adj, s, t):
        q = queue.Queue()
        self.col[s] = 'gray'
        self.dis[s] = 0
        self.par[s] = None
        q.put(s)

        while not q.empty():
            u = q.get()
            for v in adj[u]:
                if self.col[v] == 'white':
                    self.col[v] = 'gray'
                    self.dis[v] = self.dis[u] + 1
                    self.par[v] = u
                    q.put(v)
            self.col[u] = 'black'

        if self.dis[t] < self.n:
            return self.dis[t]

        return -1

if __name__ == '__main__':
    # f = open("test.txt")
    # input = f.read()
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    d = Bfs()
    print(d.distance(adj, s, t))
