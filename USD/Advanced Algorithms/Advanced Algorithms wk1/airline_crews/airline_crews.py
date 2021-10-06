# python3
import queue


class Edge:

    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0


class MaxMatching:

    def __init__(self):
        self.n = n + m + 2
        self.edges = []


    def add_edge(self, from_, to, capacity):
        forward_edge = Edge(from_, to, capacity)
        backward_edge = Edge(to, from_, 0)
        self.edges.append(forward_edge)
        self.edges.append(backward_edge)

    def add_flow(self, id, flow):
        self.edges[id].flow += flow
        self.edges[id].capacity -= flow
        self.edges[id ^ 1].flow -= flow
        self.edges[id ^ 1].capacity += flow

    def get_ids(self, from_):
        return self.graph[from_]

    def get_edge(self, id):
        return self.edges[id]

    def bfs(self, adj, edges, s, t, arr, parent):
        q = queue.Queue()
        self.col = ['white' for i in range(self.n)]
        self.col[s] = 'gray'
        parent[s] = None
        q.put(s)

        while not q.empty():
            u = q.get()
            b = 0
            for c in range(u):
                b += len(adj[c])
            b *= 2
            for x in range(len(adj[u]) * 2):
                if self.col[edges[x + b].v] == 'white' and edges[x + b].capacity > 0:
                    self.col[edges[x + b].v] = 'gray'
                    parent[edges[x + b].v] = u
                    q.put(edges[x + b].v)
                    if 0 < edges[x + b].u < n+1:
                        arr[edges[x + b].u - 1] = edges[x + b].v - n
                # elif self.col[edges[x + b].v] == 'white' and edges[x + b + 1].capacity > 0:
                #     self.col[edges[x + b].v] = 'gray'
                #     parent[edges[x + b].v] = u
                #     if 0 < edges[x + b].u < n+1 and edges[x + b].v - n not in arr:
                #         arr[u] = edges[x + b].v - n
                #     q.put(edges[x + b + 1].v)
            self.col[u] = 'black'

        return True if self.col[t] != 'white' else False

    def read_data(self):
        # f = open("./tests/01")
        # g = f.readline()
        # n, m = map(int, g.split())
        # adj_matrix = [list(map(int, f.readline().split())) for i in range(n)]
        n, m = map(int, input().split())
        adj_matrix = [list(map(int, input().split())) for i in range(n)]
        adj_matrix.insert(0, [1] * n)
        for _ in range(m):
            adj_matrix.append([1])
        adj_matrix.append([])
        return adj_matrix

    def write_response(self, matching):
        line = [str(-1 if x == -1 else x + 1) for x in matching]
        print(' '.join(line))

    def find_matching(self, adj_matrix):
        parent = [None for i in range(self.n)]
        arr = [-1] * n
        d = MaxMatching()
        while d.bfs(adj_matrix, self.edges, 0, m + n + 1, arr, parent):
            k = m + n + 1
            while k != 0:
                u = parent[k]
                b = 0
                for x in range(u):
                    b += len(adj_matrix[x])
                b *= 2
                for x in range(len(adj_matrix[u])):
                    if self.edges[b + x * 2].v == k and self.edges[b + x * 2].capacity > 0:
                        self.add_flow(b + x * 2, 1)
                    elif self.edges[1 + b + x * 2].capacity > 0:
                        self.add_flow(b + x * 2, 1)
                k = parent[k]
        return arr

    def solve(self):
        # adj_matrix = self.read_data()
        for x in range(n):
            self.add_edge(0, x + 1, 1)
        for x in range(1, n + 1):
            for j in range(m):
                capacity = 0
                if adj_matrix[x][j] == 1:
                    capacity = 1
                self.add_edge(x, n + 1 + j, capacity)
        for x in range(m):
            self.add_edge(n + 1 + x, n + m + 1, 1)
        matching = self.find_matching(adj_matrix)
        print(*matching)
        # self.write_response(matching)


f = open("./tests/08")
g = f.readline()
n, m = map(int, g.split())
edge_count = n * m
adj_matrix = [list(map(int, f.readline().split())) for i in range(n)]
adj_matrix.insert(0, [1] * n)
for _ in range(m):
    adj_matrix.append([1])
adj_matrix.append([])
max_matching = MaxMatching()
max_matching.solve()
# if __name__ == '__main__':
#     max_matching = MaxMatching()
#     max_matching.solve()
