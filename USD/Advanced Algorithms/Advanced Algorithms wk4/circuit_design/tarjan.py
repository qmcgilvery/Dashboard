# Python program to find strongly connected components in a given
# directed graph using Tarjan's algorithm (single DFS)
# Complexity : O(V+E)

from collections import defaultdict


# This class represents an directed graph
# using adjacency list representation
class Graph:

    def __init__(self, vertices):
        # No. of vertices
        self.V = vertices

        # default dictionary to store graph
        self.graph = defaultdict(list)

        self.Time = 0

    # function to add an edge to graph
    def addEdge(self, u, v):
        if v not in self.graph:
            self.graph[v].append("None")
        if "None" in self.graph[u]:
            self.graph[u] = [v]
        else:
            self.graph[u].append(v)

    '''A recursive function that find finds and prints strongly connected
    components using DFS traversal
    u --> The vertex to be visited next
    disc[] --> Stores discovery times of visited vertices
    low[] -- >> earliest visited vertex (the vertex with minimum
                discovery time) that can be reached from subtree
                rooted with current vertex
    st -- >> To store all the connected ancestors (could be part
        of SCC)
    stackMember[] --> bit/index array for faster check whether
                a node is in stack
    '''

    def SCCUtil(self, u, low, disc, stackMember, st):

        # Initialize discovery time and low value
        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1
        stackMember[u] = True
        st.append(u)

        # Go through all vertices adjacent to this
        for v in self.graph[u]:

            # If v is not visited yet, then recur for it
            if v != "None" and disc[v] == -1:

                self.SCCUtil(v, low, disc, stackMember, st)

                # Check if the subtree rooted with v has a connection to
                # one of the ancestors of u
                # Case 1 (per above discussion on Disc and Low value)
                low[u] = min(low[u], low[v])

            elif v != "None" and stackMember[v] == True:

                '''Update low value of 'u' only if 'v' is still in stack
                (i.e. it's a back edge, not cross edge).
                Case 2 (per above discussion on Disc and Low value) '''
                low[u] = min(low[u], disc[v])

            # head node found, pop the stack and print an SCC
        w = -1  # To store stack extracted vertices
        if low[u] == disc[u]:
            while w != u:
                w = st.pop()
                print(w)
                stackMember[w] = False
            print('')

        # The function to do DFS traversal.

    # It uses recursive SCCUtil()
    def SCC(self):

        # Mark all the vertices as not visited
        # and Initialize parent and visited,
        # and ap(articulation point) arrays
        disc = [-1] * (self.V)
        low = [-1] * (self.V)
        stackMember = [False] * (self.V)
        st = []

        # Call the recursive helper function
        # to find articulation points
        # in DFS tree rooted with vertex 'i'
        for i in self.graph:
            if disc[i] == -1:
                self.SCCUtil(i, low, disc, stackMember, st)

            # Create a graph given in the above diagram

f = open("test/02")
n, m = map(int, f.readline().split())
clauses = [ list(map(int, f.readline().split())) for i in range(m) ]
edges = []
vertex = [x for i in range(1, m+1) for x in (i, -i)]
g = Graph(6)
# edges = [[-1, -3], [3, 1], [1, 2], [-2, -1], [2, -3], [3, -2]]
for x,y in clauses:
    g.addEdge(x,y)
    # g.addEdge(x,-y)
g.SCC()

print(g)


# This code is contributed by Neelam Yadav
