# python3
import sys
import threading
import time
from collections import defaultdict

from typing import List, Any

sys.setrecursionlimit(10 ** 6)  # max depth of recursion
threading.stack_size(2 ** 30)  # new thread will get stack of such size


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.transposed = defaultdict(list)

    def addEdge(self, u, v):
        if v not in self.graph:
            self.graph[v].append("None")
        if "None" in self.graph[u]:
            self.graph[u] = [v]
        elif v not in self.graph[u]:
            self.graph[u].append(v)

    def fillOrder(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if i != "None" and not visited[i]:
                self.fillOrder(i, visited, stack)
        stack.append(v)

    def getTranspose(self):
        g = Graph(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j, i)
        return g

    def DFSUtil(self, v, visited, x, scc):
        visited[v] = True
        scc[x].add(v)
        if -v in scc[x]:
            scc[x].add("UNSATISFIABLE")
        for i in self.graph[v]:
            if i != "None" and not visited[i]:
                self.DFSUtil(i, visited, x, scc)

    def SCCs(self, gr):
        stack = []
        visited = {k: False for k in self.graph}
        for i in self.graph:
            if not visited[i]:
                self.fillOrder(i, visited, stack)

        scc = []
        x = 0
        visited = {k: False for k in self.graph}
        while stack:
            i = stack.pop()
            if visited[i] == False:
                scc.append(set())
                gr.DFSUtil(i, visited, x, scc)
                if "UNSATISFIABLE" in scc[x]:
                    return "UNSATISFIABLE"
                x += 1
        return scc


def results(scc):
    ans = {k: 'None' for k in range(1, n+1)}
    for x in range(len(scc) - 1, -1, -1):
        for y in scc[x]:
            if ans[abs(y)] == 'None':
                if y > 0:
                    ans[y] = 1
                else:
                    ans[abs(y)] = 0
    new_ans = []
    for x in ans:
        if ans[x] == 0:
            new_ans.append(-x)
        else:
            new_ans.append(x)
    print("SATISFIABLE")
    return new_ans


# n, m = map(int, input().split())
# clauses = [list(map(int, input().split())) for i in range(m)]
f = open("test/04")
n, m = map(int, f.readline().split())
clauses = [list(map(int, f.readline().split())) for i in range(m)]

# vertex = [x for i in range(1, m + 1) for x in (i, -i)]

graph = Graph(m * 2)
edges = []
for i in range(m):
    if len(clauses[i]) > 1:
        c1 = [-clauses[i][0], clauses[i][1]]
        c2 = [-clauses[i][1], clauses[i][0]]
        edges.append(c1)
        edges.append(c2)
    else:
        c3 = [-clauses[i][0], clauses[i][0]]
        edges.append(c3)

g = Graph(m * 2)
for x, y in edges:
    graph.addEdge(x, y)
    g.addEdge(y,x)


def main():
    scc = graph.SCCs(g)
    if scc == "UNSATISFIABLE":
        print("UNSATISFIABLE")
    else:
        res = results(scc)
        print(*res)

# start_time = time.time()
threading.Thread(target=main).start()
# print("--- %s seconds ---" % (time.time() - start_time))
