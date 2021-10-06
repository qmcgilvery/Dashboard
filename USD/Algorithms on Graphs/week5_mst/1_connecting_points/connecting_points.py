#Uses python3
import sys
import math


class Prim(object):

    def __init__(self):
        self.n = n
        self.dis = [999999999999 for i in range(self.n)]
        self.par = [None for i in range(self.n)]

    def points(self, x, y):
        q = {}
        self.dis[0] = 0

        for i in range(len(self.dis)):
            q[i] = (self.dis[i])

        m = 0
        while q:
            u = min(q, key=q.get)
            del q[u]

            for d in range(self.n):
                if self.dis[d] > math.sqrt((x[u] - x[d])**2 + (y[u] - y[d])**2) and d in q:
                    self.dis[d] = math.sqrt((x[u] - x[d])**2 + (y[u] - y[d])**2)
                    q[d] = self.dis[d]
        return sum(self.dis)

    def minimum_distance(x, y):
        result = 0.
        #write your code here
        return result


if __name__ == '__main__':
    # f = open("test.txt")
    # input = f.read()
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    p = Prim()
    print(p.points(x, y))
    # print("{0:.9f}".format(p.points(x, y)))
