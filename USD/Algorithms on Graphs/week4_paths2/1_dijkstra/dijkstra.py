#Uses python3

import sys
import queue


class Dijkstra(object):

    def __init__(self):
        self.n = len(adj)
        self.dis = [999999999999 for i in range(self.n)]

    def distance(self, adj, cost, s, t):
        q = {}
        self.dis[s] = 0

        for i in range(len(self.dis)):
            q[i] = (self.dis[i])

        while q:
            u = min(q)
            del q[u]

            for v in adj[u]:
                if self.dis[v] > self.dis[u] + cost[u][adj[u].index(v)]:
                    self.dis[v] = self.dis[u] + cost[u][adj[u].index(v)]
                    q[v] = self.dis[v]

        if self.dis[t] < 999999999999:
            return self.dis[t]

        return -1


if __name__ == '__main__':
    # f = open("test.txt")
    # input = f.read()
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    d = Dijkstra()
    print(d.distance(adj, cost, s, t))
