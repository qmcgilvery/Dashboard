# python3


class MaxMatching:
    def __init__(self, graph):

        self.graph = graph
        self.crews = len(graph[0])
        self.flights = len(graph)

    def bpm(self, u, flight, seen):

        for v in range(self.crews):
            if self.graph[u][v] and seen[v] == False:
                seen[v] = True
                if flight[v] == -1 or self.bpm(flight[v], flight, seen):
                    flight[v] = u
                    return True
        return False

    def maxBPM(self):

        flight = [-1] * self.crews

        result = 0
        for i in range(self.flights):
            seen = [False] * self.crews
            if self.bpm(i, flight, seen):
                result += 1
        matches = [1 + i if i >= 0 else i for i in flight]
        x = 1
        arr = []
        for _ in range(self.flights):
            if x in matches:
                arr.append(matches.index(x)+1)
            else:
                arr.append(-1)
            x += 1
        return arr


# f = open("./tests/09")
# g = f.readline()
# n, m = map(int, g.split())
# edge_count = n * m
# adj_matrix = [list(map(int, f.readline().split())) for _ in range(n)]
# max_matching = MaxMatching(adj_matrix)
# print(*max_matching.maxBPM())

if __name__ == '__main__':
    n, m = map(int, input().split())
    adj_matrix = [list(map(int, input().split())) for i in range(n)]
    rez = [[adj_matrix[j][i] for j in range(len(adj_matrix))] for i in range(len(adj_matrix[0]))]
    max_matching = MaxMatching(adj_matrix)
    print(*max_matching.maxBPM())
