#uses python3

import sys
import threading

# This code is used to avoid stack overflow issues
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size


class Vertex:
    def __init__(self, weight):
        self.weight = weight
        self.children = []


def ReadTree():
    size = int(input())
    tree = [Vertex(w) for w in map(int, input().split())]
    for i in range(1, size):
        a, b = list(map(int, input().split()))
        tree[a - 1].children.append(b - 1)
        tree[b - 1].children.append(a - 1)
    return tree
    # f = open("test/02")
    # size = int(f.readline())
    # tree = [Vertex(w) for w in map(int, f.readline().split())]
    # # size = int(input())
    # # tree = [Vertex(w) for w in map(int, input().split())]
    # for i in range(1, size):
    #     a, b = list(map(int, f.readline().split()))
    #     tree[a - 1].children.append(b - 1)
    #     tree[b - 1].children.append(a - 1)
    # return tree


memo = {}


def dfs(tree, vertex, parent, m0, m1, used, mw):
    if mw == 0:
        if len(tree[vertex].children) < 1:
            mw = tree[vertex].weight
        else:
            m1 = tree[vertex].weight
            for child in tree[vertex].children:
                if child != parent:
                    for gc in tree[child].children:
                        if gc != vertex:
                            if gc not in memo:
                                memo[gc] = dfs(tree, gc, child, m0, m1, used, mw)
                            m1 += memo[gc]
            m0 = 0
            for child in tree[vertex].children:
                if child != parent:
                    if child not in memo:
                        memo[child] = dfs(tree, child, vertex, m0, m1, used, mw)
                    m0 += memo[child]
                    # m0 += dfs(tree, child, vertex, m0, m1, used, mw)
            mw = max(m1, m0)
    return mw

    # This is a template function for processing a tree using depth-first search.
    # Write your code here.
    # You may need to add more parameters to this function for child processing.


def MaxWeightIndependentTreeSubset(tree):
    size = len(tree)
    if size == 0:
        return 0
    x = dfs(tree, 0, -1, 0, 0, [], 0)
    # You must decide what to return.
    return x


def main():
    ans = []
    tree = ReadTree();
    weight = MaxWeightIndependentTreeSubset(tree);
    ans.append(weight)
    print(*ans)


# main()
# This is to avoid stack overflow issues
threading.Thread(target=main).start()
