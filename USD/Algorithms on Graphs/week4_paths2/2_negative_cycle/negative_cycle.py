# Uses python3

import sys


class BellmanFord(object):

    def __init__(self):
        self.n = len(adj)
        self.ver = [999999999999 for i in range(self.n)]
        self.dis = [999999999999 for i in range(self.n)]

    def negative_cycle(self, adj, cost):
        q = {}
        self.dis[0] = 0
        for _ in range(n-1):
            for u in range(n):
                for v in adj[u]:
                    if self.dis[v] > self.dis[u] + cost[u][adj[u].index(v)]:
                        self.dis[v] = self.dis[u] + cost[u][adj[u].index(v)]
        for u in range(n):
            for v in adj[u]:
                if self.dis[v] > self.dis[u] + cost[u][adj[u].index(v)]:
                    return 1
        return 0


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
    neg = BellmanFord()
    print(neg.negative_cycle(adj, cost))
