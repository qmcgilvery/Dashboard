# python3
from collections import defaultdict
import queue


class Edge:

    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0


# This class implements a bit unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.

class FlowGraph:

    def __init__(self, n):
        # List of all - forward and backward - edges
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(n)]
        # adj = [[] for _ in range(n)]

    def add_edge(self, from_, to, capacity):
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
        forward_edge = Edge(from_, to, capacity)
        backward_edge = Edge(to, from_, 0)
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)

    def size(self):
        return len(self.graph)

    def get_ids(self, from_):
        return self.graph[from_]

    def get_edge(self, id):
        return self.edges[id]

    def add_flow(self, id, flow):
        # To get a backward edge for a true forward edge (i.e id is even), we should get id + 1
        # due to the described above scheme. On the other hand, when we have to get a "backward"
        # edge for a backward edge (i.e. get a forward edge for backward - id is odd), id - 1
        # should be taken.
        #
        # It turns out that id ^ 1 works for both cases. Think this through!
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow


class Vertex(object):

    def __init__(self, graph):
        self.n = len(graph.graph)
        self.color = ['white' for i in range(self.n)]
        self.order = []


    def dfs(self, adj, edges, x, paths):

        self.color[x] = 'gray'
        self.order.append(x)
        if x == self.n - 1:
            path = self.order[:]
            paths.append(path)
        else:
            for z in adj[x]:
                if self.color[edges[z].v] == 'white' and edges[z].v != edges[z].u and edges[z].capacity > 0:
                    self.dfs(adj, edges, edges[z].v, paths)
        self.order.pop()
        self.color[x] = 'white'

        return paths

    def bfs(self, adj, edges, s, t):
        q = queue.Queue()
        self.col = ['white' for i in range(self.n)]
        self.dis = [n + 1 for i in range(self.n)]
        self.par = [None for i in range(self.n)]
        self.col[s] = 'gray'
        self.dis[s] = 0
        self.par[s] = None
        q.put(s)

        while not q.empty():
            u = q.get()
            for z in adj[u]:
                if self.col[edges[z].v] == 'white' and edges[z].capacity > 0 and edges[z].v != edges[z].u:
                    self.col[edges[z].v] = 'gray'
                    self.dis[edges[z].v] = self.dis[u] + 1
                    self.par[edges[z].v] = u
                    q.put(edges[z].v)
            self.col[u] = 'black'

        # return self.par if self.col[t] != 'white' else False
        return True if self.col[t] != 'white' else False

    def bfs2(self, adj, edges, s, t):
        # q = queue.Queue()
        # self.col = ['white' for i in range(self.n)]
        # self.dis = [n + 1 for i in range(self.n)]
        # self.par = [None for i in range(self.n)]
        # self.col[s] = 'gray'
        # self.dis[s] = 0
        # self.par[s] = None
        # q.put(s)
        #
        # while not q.empty():
        #     u = q.get()
        #     for z in adj[u]:
        #         if self.col[edges[z].v] == 'white' and edges[z].capacity > 0:
        #             self.col[edges[z].v] = 'gray'
        #             self.dis[edges[z].v] = self.dis[u] + 1
        #             self.par[edges[z].v] = u
        #             q.put(edges[z].v)
        #     self.col[u] = 'black'
        #
        # # return self.par if self.col[t] != 'white' else False
        return self.par


def get_ids(self, from_):
    return self.graph[from_]


def get_edge(self, id):
    return self.edges[id]


def add_flow(self, id, flow):
    # To get a backward edge for a true forward edge (i.e id is even), we should get id + 1
    # due to the described above scheme. On the other hand, when we have to get a "backward"
    # edge for a backward edge (i.e. get a forward edge for backward - id is odd), id - 1
    # should be taken.
    #
    # It turns out that id ^ 1 works for both cases. Think this through!
    self.edges[id].flow += flow
    graph.edges[id].capacity -= flow
    self.edges[id ^ 1].flow -= flow
    graph.edges[id ^ 1].capacity += flow


def read_data():
    f = open("./tests/10")
    p = f.readline().split()
    vertex_count, edge_count = map(int, p)
    graph = FlowGraph(vertex_count)
    for _ in range(edge_count):
        x = f.readline().split()
        u, v, capacity = map(int, x)
        graph.add_edge(u - 1, v - 1, capacity)
    return graph


# def read_data():
#     vertex_count, edge_count = map(int, input().split())
#     graph = FlowGraph(vertex_count)
#     for _ in range(edge_count):
#         u, v, capacity = map(int, input().split())
#         graph.add_edge(u - 1, v - 1, capacity)
#     return graph


def max_flow(graph, from_, to):
    flow = 0
    d = Vertex(graph)
    parent = [-1] * n
    while d.bfs(graph.graph, graph.edges, 0, to):
        parent = d.bfs2(graph.graph, graph.edges, 0, to)
        path_flow = float("Inf")
        t = to
        while t != from_:
            p = get_ids(graph, parent[t])
            for x in p:
                if graph.edges[x].v == t and graph.edges[x].capacity > 0:
                    g = get_edge(graph, x)
                    path_flow = min(path_flow, g.capacity)
                    t = parent[t]

        flow += path_flow

        k = to
        while k != from_:
            c = [False for i in range(k)]
            u = parent[k]
            p = get_ids(graph, u)
            for x in (p):
                # next = graph.edges[p[x+1]].v
                if graph.edges[x].v == k and c[k-1] != True and graph.edges[x].capacity > 0:
                    c[k-1] = True
                    add_flow(graph, x, path_flow)
                    # if next == k:
                    #     break

            k = parent[k]

    return flow



if __name__ == '__main__':
    graph = read_data()
    n = len(graph.graph)
    print(max_flow(graph, 0, graph.size() - 1))
