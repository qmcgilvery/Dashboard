import networkx as nx
from itertools import permutations


# This function takes as input a graph g and a list of vertices of the cycle.
# (Each vertex given by its index starting from 0.)
# The graph is complete (i.e., each pair of distinct vertices is connected by an edge),
# undirected (i.e., the edge from u to v has the same weight as the edge from v to u),
# and has no self-loops (i.e., there are no edges from i to i).
#
# For example, a valid input would be a graph on 3 vertices and cycle = [2, 0, 1].
#
# The function should return the weight of the cycle.
# (Don't forget to add up the last edge connecting the last vertex of the cycle with the first one.)
#
# If you want to get the weight of the edge between vertices u and v, you can take g[u][v]['weight']


def cycle_length(g, cycle):
    # Checking that the number of vertices in the graph equals the number of vertices in the cycle.
    assert len(cycle) == g.number_of_nodes()
    # Write your code here.
    return sum(g[cycle[i]][cycle[i + 1]]['weight'] for i in range(len(cycle) - 1)) + g[cycle[0]][cycle[-1]]['weight']


# Here is a test case:
# Create an empty graph.
g = nx.Graph()
# Now we will add 6 edges between 4 vertices
g.add_edge(0, 1, weight=20)
# We work with undirected graphs, so once we add an edge from 0 to 1, it automatically creates an edge of the same weight from 1 to 0.
g.add_edge(1, 2, weight=2)
g.add_edge(2, 3, weight=2)
g.add_edge(3, 0, weight=2)
g.add_edge(0, 2, weight=1)
g.add_edge(1, 3, weight=1)

# Now we want to compute the lengths of two cycles:
cycle1 = [0, 1, 2, 3]
cycle2 = [0, 2, 1, 3]


# assert(cycle_length(g, cycle1) == 8)
# assert(cycle_length(g, cycle2) == 6)

# This function takes as input a graph g.
# The graph is complete (i.e., each pair of distinct vertices is connected by an edge),
# undirected (i.e., the edge from u to v has the same weight as the edge from v to u),
# and has no self-loops (i.e., there are no edges from i to i).
#
# The function should return the weight of a shortest Hamiltonian cycle.
# (Don't forget to add up the last edge connecting the last vertex of the cycle with the first one.)
#
# You can iterate through all permutations of the set {0, ..., n-1} and find a cycle of the minimum weight.


def all_permutations(g):
    # n is the number of vertices.
    n = g.number_of_nodes()
    opt = 0
    d = 0
    # Iterate through all permutations of n vertices
    for p in permutations(range(n)):
        opt += cycle_length(g, p)
        d += 1

    return opt/d


def nearest_neighbors(g):
    current_node = 0
    path = [current_node]
    n = g.number_of_nodes()
    nodes = g.nodes()
    # We'll repeat the same routine (n-1) times
    for _ in range(n - 1):
        next_node = None
        # The distance to the closest vertex. Initialized with infinity.
        min_edge = float("inf")
        v = 1
        for v in g.nodes():
            if current_node != v:
                # print(g[current_node][v]['weight'])
                if g[current_node][v]['weight'] < min_edge and v not in path:
                    # print(g[current_node][v]['weight'])
                    next_node = v
                    min_edge = g[current_node][v]['weight']
            v+=1
            # if g.node[current_node][v]['weight'] < min_edge and v not in path:
                # Write your code here: decide if v is a better candidate than next_node.
                # If it is, then update the values of next_node and min_edge
                # next_node = v
                # min_edge = g[path][v]['weight']

        assert next_node is not None
        path.append(next_node)
        current_node = next_node

    weight = sum(g[path[i]][path[i + 1]]['weight'] for i in range(g.number_of_nodes() - 1))
    weight += g[path[-1]][path[0]]['weight']
    return weight


print(nearest_neighbors(g))
